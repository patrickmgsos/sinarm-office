"""Tests for configuration selectors."""

from __future__ import annotations

import pytest

from apps.common.models import ArchivableModel
from apps.configuration.models import SystemSetting
from apps.configuration.selectors import (
    get_organization_setting_value,
    get_system_setting_value,
    organization_settings_active,
    system_settings_active,
)
from apps.configuration.services import set_organization_setting, set_system_setting
from apps.organization.models import Organization

pytestmark = pytest.mark.django_db


def test_system_settings_active_excludes_archived_records() -> None:
    """Selector should return only active system settings."""
    active = set_system_setting(key="active_setting", name="Active", value=True)
    archived = set_system_setting(key="archived_setting", name="Archived", value=True)
    archived.status = ArchivableModel.ArchiveStatus.ARCHIVED
    archived.save(update_fields=["status"])

    assert list(system_settings_active()) == [active]


def test_organization_settings_active_filters_by_organization() -> None:
    """Selector should return active settings for one organization."""
    organization = Organization.objects.create(name="SINARM Office")
    other = Organization.objects.create(name="Other")
    expected = set_organization_setting(
        organization=organization,
        key="timezone",
        name="Timezone",
        value="America/Sao_Paulo",
    )
    set_organization_setting(
        organization=other,
        key="timezone",
        name="Timezone",
        value="UTC",
    )

    assert list(organization_settings_active(organization_id=organization.id)) == [
        expected
    ]


def test_value_selectors_return_typed_values_or_default() -> None:
    """Value selectors should return typed values and respect defaults."""
    organization = Organization.objects.create(name="SINARM Office")
    set_system_setting(key="enabled", name="Enabled", value=True)
    set_organization_setting(
        organization=organization,
        key="page_size",
        name="Page size",
        value=30,
    )

    assert get_system_setting_value(key="enabled") is True
    assert (
        get_organization_setting_value(
            organization_id=organization.id,
            key="page_size",
        )
        == 30
    )
    assert get_system_setting_value(key="missing", default="fallback") == "fallback"


def test_archived_setting_value_is_not_returned() -> None:
    """Value selector should ignore archived settings."""
    setting = set_system_setting(key="hidden", name="Hidden", value="value")
    setting.status = ArchivableModel.ArchiveStatus.ARCHIVED
    setting.save(update_fields=["status"])

    assert get_system_setting_value(key="hidden", default=None) is None
    assert SystemSetting.objects.count() == 1
