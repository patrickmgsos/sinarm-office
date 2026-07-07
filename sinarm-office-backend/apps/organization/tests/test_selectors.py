"""Tests for organization selectors."""

from __future__ import annotations

import pytest

from apps.common.models import ArchivableModel
from apps.organization.models import Department, Office, Organization
from apps.organization.selectors import (
    departments_for_office,
    departments_for_organization,
    offices_for_organization,
    organizations_active,
)

pytestmark = pytest.mark.django_db


def test_organizations_active_excludes_archived_records() -> None:
    """Selector should return only active organizations."""
    active = Organization.objects.create(name="Active")
    Organization.objects.create(
        name="Archived",
        status=ArchivableModel.ArchiveStatus.ARCHIVED,
    )

    assert list(organizations_active()) == [active]


def test_offices_for_organization_filters_by_organization() -> None:
    """Selector should return offices for one organization."""
    organization = Organization.objects.create(name="SINARM Office")
    other = Organization.objects.create(name="Other")
    expected = Office.objects.create(
        organization=organization,
        name="Headquarters",
        code="hq",
    )
    Office.objects.create(organization=other, name="Other Office", code="other")

    assert list(offices_for_organization(organization_id=organization.id)) == [expected]


def test_departments_selectors_filter_scope() -> None:
    """Selectors should filter departments by organization or office."""
    organization = Organization.objects.create(name="SINARM Office")
    office = Office.objects.create(
        organization=organization,
        name="Headquarters",
        code="hq",
    )
    expected = Department.objects.create(
        organization=organization,
        office=office,
        name="Operations",
        code="ops",
    )

    assert list(departments_for_organization(organization_id=organization.id)) == [
        expected
    ]
    assert list(departments_for_office(office_id=office.id)) == [expected]
