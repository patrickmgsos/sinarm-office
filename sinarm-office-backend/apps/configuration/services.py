"""Application services for technical configuration settings."""

from __future__ import annotations

from decimal import Decimal
from typing import Any

from django.db import transaction
from django.utils import timezone

from apps.common.models import ArchivableModel
from apps.configuration.models import OrganizationSetting, SystemSetting
from apps.organization.models import Organization

SettingValue = str | bool | int | Decimal | dict[str, Any]


def _prepare_setting_value(
    setting: SystemSetting | OrganizationSetting,
    *,
    value: SettingValue,
) -> None:
    """Set and validate a typed setting value."""
    setting.set_value(value)
    setting.full_clean()


@transaction.atomic
def set_system_setting(
    *,
    key: str,
    name: str,
    value: SettingValue,
    description: str = "",
) -> SystemSetting:
    """Create or update a platform-wide setting."""
    setting, _created = SystemSetting.objects.get_or_create(
        key=key,
        defaults={"name": name, "description": description},
    )
    setting.name = name
    setting.description = description
    _prepare_setting_value(setting, value=value)
    setting.save()
    return setting


@transaction.atomic
def set_organization_setting(
    *,
    organization: Organization,
    key: str,
    name: str,
    value: SettingValue,
    description: str = "",
) -> OrganizationSetting:
    """Create or update an organization-scoped setting."""
    setting, _created = OrganizationSetting.objects.get_or_create(
        organization=organization,
        key=key,
        defaults={"name": name, "description": description},
    )
    setting.name = name
    setting.description = description
    _prepare_setting_value(setting, value=value)
    setting.save()
    return setting


@transaction.atomic
def archive_system_setting(setting: SystemSetting) -> SystemSetting:
    """Archive a system setting without deleting it."""
    setting.status = ArchivableModel.ArchiveStatus.ARCHIVED
    setting.archived_at = timezone.now()
    setting.save(update_fields=["status", "archived_at", "updated_at"])
    return setting


@transaction.atomic
def archive_organization_setting(
    setting: OrganizationSetting,
) -> OrganizationSetting:
    """Archive an organization setting without deleting it."""
    setting.status = ArchivableModel.ArchiveStatus.ARCHIVED
    setting.archived_at = timezone.now()
    setting.save(update_fields=["status", "archived_at", "updated_at"])
    return setting
