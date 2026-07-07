"""Tests for configuration services."""

from __future__ import annotations

from decimal import Decimal

import pytest

from apps.common.models import ArchivableModel
from apps.configuration.models import SystemSetting
from apps.configuration.services import (
    archive_organization_setting,
    archive_system_setting,
    set_organization_setting,
    set_system_setting,
)
from apps.organization.models import Organization

pytestmark = pytest.mark.django_db


def test_set_system_setting_creates_and_updates_typed_value() -> None:
    """Service should create and update a system setting by key."""
    setting = set_system_setting(
        key="page_size",
        name="Page size",
        value=25,
    )
    updated = set_system_setting(
        key="page_size",
        name="Page size",
        value=50,
    )

    assert setting.id == updated.id
    assert updated.value_type == SystemSetting.ValueType.INTEGER
    assert updated.get_value() == 50


def test_set_organization_setting_creates_scoped_value() -> None:
    """Service should create settings scoped to an organization."""
    organization = Organization.objects.create(name="SINARM Office")
    setting = set_organization_setting(
        organization=organization,
        key="tax_rate",
        name="Tax rate",
        value=Decimal("1.500000"),
    )

    assert setting.organization == organization
    assert setting.get_value() == Decimal("1.500000")


def test_archive_services_mark_settings_as_archived() -> None:
    """Archive services should preserve configuration history."""
    organization = Organization.objects.create(name="SINARM Office")
    system_setting = set_system_setting(
        key="system_mode",
        name="System mode",
        value="normal",
    )
    organization_setting = set_organization_setting(
        organization=organization,
        key="locale",
        name="Locale",
        value="pt-br",
    )

    archive_system_setting(system_setting)
    archive_organization_setting(organization_setting)

    assert system_setting.status == ArchivableModel.ArchiveStatus.ARCHIVED
    assert organization_setting.status == ArchivableModel.ArchiveStatus.ARCHIVED
