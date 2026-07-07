"""Django admin configuration for configuration models."""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeAlias

from django.contrib import admin

from apps.configuration.models import OrganizationSetting, SystemSetting

if TYPE_CHECKING:
    # fmt: off
    SystemSettingAdminBase: TypeAlias = admin.ModelAdmin[SystemSetting]  # noqa: UP040
    OrganizationSettingAdminBase: TypeAlias = (  # noqa: UP040
        admin.ModelAdmin[OrganizationSetting]
    )
    # fmt: on
else:
    SystemSettingAdminBase = admin.ModelAdmin
    OrganizationSettingAdminBase = admin.ModelAdmin


@admin.register(SystemSetting)
class SystemSettingAdmin(SystemSettingAdminBase):
    """Admin for platform-wide settings."""

    list_display = ("key", "name", "value_type", "status", "updated_at")
    list_filter = ("value_type", "status")
    search_fields = ("key", "name", "description")
    readonly_fields = ("id", "created_at", "updated_at")


@admin.register(OrganizationSetting)
class OrganizationSettingAdmin(OrganizationSettingAdminBase):
    """Admin for organization-scoped settings."""

    list_display = ("key", "organization", "name", "value_type", "status")
    list_filter = ("value_type", "status", "organization")
    search_fields = ("key", "name", "description", "organization__name")
    readonly_fields = ("id", "created_at", "updated_at")
