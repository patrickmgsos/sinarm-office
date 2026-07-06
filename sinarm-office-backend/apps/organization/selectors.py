"""Query helpers for technical organization records."""

from __future__ import annotations

import uuid

from django.db.models import QuerySet

from apps.common.models import ArchivableModel
from apps.organization.models import Department, Office, Organization


def organizations_active() -> QuerySet[Organization]:
    """Return active organizations."""
    return Organization.objects.filter(
        status=ArchivableModel.ArchiveStatus.ACTIVE,
    ).order_by("name")


def offices_for_organization(
    *,
    organization_id: uuid.UUID,
    active_only: bool = True,
) -> QuerySet[Office]:
    """Return offices for an organization."""
    queryset = Office.objects.filter(organization_id=organization_id).select_related(
        "organization",
    )
    if active_only:
        queryset = queryset.filter(status=ArchivableModel.ArchiveStatus.ACTIVE)

    return queryset.order_by("name")


def departments_for_organization(
    *,
    organization_id: uuid.UUID,
    active_only: bool = True,
) -> QuerySet[Department]:
    """Return departments for an organization."""
    queryset = Department.objects.filter(
        organization_id=organization_id,
    ).select_related("organization", "office")
    if active_only:
        queryset = queryset.filter(status=ArchivableModel.ArchiveStatus.ACTIVE)

    return queryset.order_by("name")


def departments_for_office(
    *,
    office_id: uuid.UUID,
    active_only: bool = True,
) -> QuerySet[Department]:
    """Return departments for a specific office."""
    queryset = Department.objects.filter(office_id=office_id).select_related(
        "organization",
        "office",
    )
    if active_only:
        queryset = queryset.filter(status=ArchivableModel.ArchiveStatus.ACTIVE)

    return queryset.order_by("name")
