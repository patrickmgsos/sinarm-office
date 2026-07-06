"""Application services for technical organization records."""

from __future__ import annotations

from django.db import transaction
from django.utils import timezone

from apps.common.models import ArchivableModel
from apps.organization.models import Department, Office, Organization


@transaction.atomic
def create_organization(
    *,
    name: str,
    legal_name: str = "",
    document_number: str = "",
    email: str = "",
    phone: str = "",
    is_default: bool = False,
) -> Organization:
    """Create an organization root."""
    return Organization.objects.create(
        name=name,
        legal_name=legal_name,
        document_number=document_number,
        email=email,
        phone=phone,
        is_default=is_default,
    )


@transaction.atomic
def create_office(
    *,
    organization: Organization,
    name: str,
    code: str,
    email: str = "",
    phone: str = "",
    is_headquarters: bool = False,
) -> Office:
    """Create an office or branch for an organization."""
    return Office.objects.create(
        organization=organization,
        name=name,
        code=code,
        email=email,
        phone=phone,
        is_headquarters=is_headquarters,
    )


@transaction.atomic
def create_department(
    *,
    organization: Organization,
    name: str,
    code: str,
    office: Office | None = None,
    description: str = "",
) -> Department:
    """Create an internal department."""
    return Department.objects.create(
        organization=organization,
        office=office,
        name=name,
        code=code,
        description=description,
    )


@transaction.atomic
def archive_organization(organization: Organization) -> Organization:
    """Archive an organization without deleting its historical records."""
    organization.status = ArchivableModel.ArchiveStatus.ARCHIVED
    organization.archived_at = timezone.now()
    organization.save(update_fields=["status", "archived_at", "updated_at"])
    return organization


@transaction.atomic
def archive_office(office: Office) -> Office:
    """Archive an office without deleting it."""
    office.status = ArchivableModel.ArchiveStatus.ARCHIVED
    office.archived_at = timezone.now()
    office.save(update_fields=["status", "archived_at", "updated_at"])
    return office


@transaction.atomic
def archive_department(department: Department) -> Department:
    """Archive a department without deleting it."""
    department.status = ArchivableModel.ArchiveStatus.ARCHIVED
    department.archived_at = timezone.now()
    department.save(update_fields=["status", "archived_at", "updated_at"])
    return department
