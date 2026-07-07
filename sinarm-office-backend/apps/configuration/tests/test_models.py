"""Tests for technical configuration models."""

from __future__ import annotations

from decimal import Decimal

import pytest
from django.core.exceptions import ValidationError
from django.db import IntegrityError

from apps.configuration.models import OrganizationSetting, SystemSetting
from apps.organization.models import Organization

pytestmark = pytest.mark.django_db


def test_system_setting_stores_typed_values() -> None:
    """System settings should preserve supported technical value types."""
    setting = SystemSetting(key="feature_flag", name="Feature flag")
    setting.set_value(True)
    setting.full_clean()
    setting.save()

    assert setting.value_type == SystemSetting.ValueType.BOOLEAN
    assert setting.get_value() is True


def test_decimal_and_json_values_are_supported() -> None:
    """Settings should support decimal and JSON values."""
    decimal_setting = SystemSetting(key="rate_limit", name="Rate limit")
    decimal_setting.set_value(Decimal("10.500000"))
    decimal_setting.full_clean()
    decimal_setting.save()

    json_setting = SystemSetting(key="ui_options", name="UI options")
    json_setting.set_value({"density": "compact"})
    json_setting.full_clean()
    json_setting.save()

    assert decimal_setting.get_value() == Decimal("10.500000")
    assert json_setting.get_value() == {"density": "compact"}


def test_secret_like_keys_are_rejected() -> None:
    """Configuration must not store sensitive secret material."""
    setting = SystemSetting(key="api_key", name="API key")
    setting.set_value("secret")

    with pytest.raises(ValidationError):
        setting.full_clean()


def test_organization_setting_key_is_unique_per_organization() -> None:
    """Organization settings should be unique within their organization scope."""
    organization = Organization.objects.create(name="SINARM Office")
    other = Organization.objects.create(name="Other")
    OrganizationSetting.objects.create(
        organization=organization,
        key="timezone",
        name="Timezone",
        value_type=OrganizationSetting.ValueType.STRING,
        string_value="America/Sao_Paulo",
    )
    OrganizationSetting.objects.create(
        organization=other,
        key="timezone",
        name="Timezone",
        value_type=OrganizationSetting.ValueType.STRING,
        string_value="UTC",
    )

    with pytest.raises(IntegrityError):
        OrganizationSetting.objects.create(
            organization=organization,
            key="timezone",
            name="Duplicate timezone",
            value_type=OrganizationSetting.ValueType.STRING,
            string_value="UTC",
        )
