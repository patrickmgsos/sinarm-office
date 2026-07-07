"""Django admin configuration for Case MVP."""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeAlias

from django.contrib import admin

from apps.cases.models import Case

if TYPE_CHECKING:
    CaseAdminBase: TypeAlias = admin.ModelAdmin[Case]  # noqa: UP040
else:
    CaseAdminBase = admin.ModelAdmin


@admin.register(Case)
class CaseAdmin(CaseAdminBase):
    """Admin for operational cases."""

    list_display = (
        "customer",
        "case_type",
        "status_type",
        "responsible_user",
        "opened_at",
        "due_date",
        "status",
    )
    list_filter = (
        "status",
        "case_type",
        "status_type",
        "responsible_user",
        "opened_at",
        "due_date",
    )
    search_fields = (
        "customer__name",
        "customer__document_number",
        "notes",
    )
    autocomplete_fields = ("customer", "case_type", "status_type", "responsible_user")
    readonly_fields = ("id", "created_at", "updated_at")
