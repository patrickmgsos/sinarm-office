"""Django admin configuration for reference data models."""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeAlias

from django.contrib import admin

from apps.reference_data.models import Caliber, FirearmModel, Manufacturer

if TYPE_CHECKING:
    ManufacturerAdminBase: TypeAlias = admin.ModelAdmin[Manufacturer]  # noqa: UP040
    CaliberAdminBase: TypeAlias = admin.ModelAdmin[Caliber]  # noqa: UP040
    FirearmModelAdminBase: TypeAlias = admin.ModelAdmin[FirearmModel]  # noqa: UP040
else:
    ManufacturerAdminBase = admin.ModelAdmin
    CaliberAdminBase = admin.ModelAdmin
    FirearmModelAdminBase = admin.ModelAdmin


@admin.register(Manufacturer)
class ManufacturerAdmin(ManufacturerAdminBase):
    """Admin for firearm manufacturers."""

    list_display = ("name", "country", "status", "created_at")
    list_filter = ("status", "country")
    search_fields = ("name", "country", "notes")
    readonly_fields = ("id", "created_at", "updated_at")


@admin.register(Caliber)
class CaliberAdmin(CaliberAdminBase):
    """Admin for calibers."""

    list_display = ("name", "category", "status", "created_at")
    list_filter = ("status", "category")
    search_fields = ("name", "category", "description")
    readonly_fields = ("id", "created_at", "updated_at")


@admin.register(FirearmModel)
class FirearmModelAdmin(FirearmModelAdminBase):
    """Admin for firearm models."""

    list_display = (
        "name",
        "manufacturer",
        "caliber",
        "species",
        "operation",
        "status",
    )
    list_filter = ("status", "manufacturer", "caliber", "species", "operation")
    search_fields = (
        "name",
        "manufacturer__name",
        "caliber__name",
        "species",
        "operation",
        "notes",
    )
    readonly_fields = ("id", "created_at", "updated_at")
