"""Django admin configuration for Firearm MVP."""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeAlias

from django.contrib import admin

from apps.firearms.models import Firearm

if TYPE_CHECKING:
    FirearmAdminBase: TypeAlias = admin.ModelAdmin[Firearm]  # noqa: UP040
else:
    FirearmAdminBase = admin.ModelAdmin


@admin.register(Firearm)
class FirearmAdmin(FirearmAdminBase):
    """Admin for operational firearms."""

    list_display = (
        "customer",
        "manufacturer",
        "model",
        "caliber",
        "serial_number",
        "sinarm_registration",
        "registration_valid_until",
        "status",
    )
    list_filter = ("status", "manufacturer", "caliber", "registration_valid_until")
    search_fields = (
        "customer__name",
        "customer__document_number",
        "serial_number",
        "sinarm_registration",
        "notes",
    )
    autocomplete_fields = ("customer", "manufacturer", "model", "caliber")
    readonly_fields = ("id", "created_at", "updated_at")
