"""Django admin configuration for organization models."""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeAlias

from django.contrib import admin

from apps.organization.models import Department, Office, Organization

if TYPE_CHECKING:
    OrganizationAdminBase: TypeAlias = admin.ModelAdmin[Organization]  # noqa: UP040
    OfficeAdminBase: TypeAlias = admin.ModelAdmin[Office]  # noqa: UP040
    DepartmentAdminBase: TypeAlias = admin.ModelAdmin[Department]  # noqa: UP040
else:
    OrganizationAdminBase = admin.ModelAdmin
    OfficeAdminBase = admin.ModelAdmin
    DepartmentAdminBase = admin.ModelAdmin


@admin.register(Organization)
class OrganizationAdmin(OrganizationAdminBase):
    """Admin for organizations."""

    list_display = ("name", "document_number", "status", "is_default", "created_at")
    list_filter = ("status", "is_default")
    search_fields = ("name", "legal_name", "document_number", "email")
    readonly_fields = ("id", "created_at", "updated_at")


@admin.register(Office)
class OfficeAdmin(OfficeAdminBase):
    """Admin for organization offices."""

    list_display = ("name", "organization", "code", "status", "is_headquarters")
    list_filter = ("status", "is_headquarters", "organization")
    search_fields = ("name", "code", "email", "organization__name")
    readonly_fields = ("id", "created_at", "updated_at")


@admin.register(Department)
class DepartmentAdmin(DepartmentAdminBase):
    """Admin for organization departments."""

    list_display = ("name", "organization", "office", "code", "status")
    list_filter = ("status", "organization", "office")
    search_fields = ("name", "code", "description", "organization__name")
    readonly_fields = ("id", "created_at", "updated_at")
