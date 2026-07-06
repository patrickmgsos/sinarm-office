"""Tests for organization services."""

from __future__ import annotations

import pytest

from apps.common.models import ArchivableModel
from apps.organization.services import (
    archive_department,
    archive_office,
    archive_organization,
    create_department,
    create_office,
    create_organization,
)

pytestmark = pytest.mark.django_db


def test_create_organization_service() -> None:
    """Service should create an organization root."""
    organization = create_organization(
        name="SINARM Office",
        legal_name="SINARM Office LTDA",
        document_number="00000000000100",
    )

    assert organization.name == "SINARM Office"
    assert organization.legal_name == "SINARM Office LTDA"


def test_create_office_and_department_services() -> None:
    """Services should create offices and departments under organization."""
    organization = create_organization(name="SINARM Office")
    office = create_office(organization=organization, name="Headquarters", code="hq")
    department = create_department(
        organization=organization,
        office=office,
        name="Operations",
        code="ops",
    )

    assert office.organization == organization
    assert department.office == office


def test_archive_services_use_archived_status() -> None:
    """Archive services should mark entities as archived without deletion."""
    organization = create_organization(name="SINARM Office")
    office = create_office(organization=organization, name="Headquarters", code="hq")
    department = create_department(
        organization=organization,
        office=office,
        name="Operations",
        code="ops",
    )

    archive_organization(organization)
    archive_office(office)
    archive_department(department)

    assert organization.status == ArchivableModel.ArchiveStatus.ARCHIVED
    assert office.status == ArchivableModel.ArchiveStatus.ARCHIVED
    assert department.status == ArchivableModel.ArchiveStatus.ARCHIVED
