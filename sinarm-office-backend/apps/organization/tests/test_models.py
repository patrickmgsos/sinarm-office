"""Tests for technical organization models."""

from __future__ import annotations

import uuid

import pytest

from apps.common.models import ArchivableModel
from apps.organization.models import Department, Office, Organization

pytestmark = pytest.mark.django_db


def test_organization_uses_uuid_and_archive_status() -> None:
    """Organization must use UUID identity and opt-in archive semantics."""
    organization = Organization.objects.create(name="SINARM Office")

    assert isinstance(organization.id, uuid.UUID)
    assert organization.status == ArchivableModel.ArchiveStatus.ACTIVE


def test_office_belongs_to_organization() -> None:
    """Office must belong to an organization."""
    organization = Organization.objects.create(name="SINARM Office")
    office = Office.objects.create(
        organization=organization,
        name="Headquarters",
        code="hq",
    )

    assert office.organization == organization


def test_department_belongs_to_organization_and_optional_office() -> None:
    """Department must belong to an organization and may belong to an office."""
    organization = Organization.objects.create(name="SINARM Office")
    office = Office.objects.create(
        organization=organization,
        name="Headquarters",
        code="hq",
    )
    department = Department.objects.create(
        organization=organization,
        office=office,
        name="Operations",
        code="ops",
    )

    assert department.organization == organization
    assert department.office == office
