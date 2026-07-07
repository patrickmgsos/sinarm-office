"""Query helpers for technical configuration settings."""

from __future__ import annotations

import uuid
from decimal import Decimal
from typing import Any

from django.db.models import QuerySet

from apps.common.models import ArchivableModel
from apps.configuration.models import OrganizationSetting, SystemSetting

SettingValue = str | bool | int | Decimal | Any | None


def system_settings_active() -> QuerySet[SystemSetting]:
    """Return active platform-wide settings."""
    return SystemSetting.objects.filter(
        status=ArchivableModel.ArchiveStatus.ACTIVE,
    ).order_by("key")


def organization_settings_active(
    *,
    organization_id: uuid.UUID,
) -> QuerySet[OrganizationSetting]:
    """Return active settings for an organization."""
    return OrganizationSetting.objects.filter(
        organization_id=organization_id,
        status=ArchivableModel.ArchiveStatus.ACTIVE,
    ).select_related("organization")


def get_system_setting_value(*, key: str, default: SettingValue = None) -> SettingValue:
    """Return a typed platform setting value or the provided default."""
    setting = system_settings_active().filter(key=key).first()
    if setting is None:
        return default

    return setting.get_value()


def get_organization_setting_value(
    *,
    organization_id: uuid.UUID,
    key: str,
    default: SettingValue = None,
) -> SettingValue:
    """Return a typed organization setting value or the provided default."""
    setting = (
        organization_settings_active(organization_id=organization_id)
        .filter(
            key=key,
        )
        .first()
    )
    if setting is None:
        return default

    return setting.get_value()
