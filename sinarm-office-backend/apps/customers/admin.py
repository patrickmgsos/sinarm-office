"""Django admin configuration for Customer Domain."""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeAlias

from django.contrib import admin

from apps.customers.models import Customer

if TYPE_CHECKING:
    CustomerAdminBase: TypeAlias = admin.ModelAdmin[Customer]  # noqa: UP040
else:
    CustomerAdminBase = admin.ModelAdmin


@admin.register(Customer)
class CustomerAdmin(CustomerAdminBase):
    """Admin for customer aggregate roots."""

    list_display = (
        "name",
        "kind",
        "document_type",
        "document_number",
        "status",
        "created_at",
    )
    list_filter = ("status", "kind", "document_type")
    search_fields = ("name", "document_number", "notes")
    readonly_fields = ("id", "created_at", "updated_at")
