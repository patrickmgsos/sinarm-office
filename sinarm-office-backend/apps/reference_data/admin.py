"""Django admin configuration for reference data models."""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeAlias

from django.contrib import admin

from apps.reference_data.models import (
    Caliber,
    CaseType,
    City,
    Country,
    DocumentType,
    FirearmModel,
    Manufacturer,
    State,
    StatusType,
    WorkflowType,
)

if TYPE_CHECKING:
    ManufacturerAdminBase: TypeAlias = admin.ModelAdmin[Manufacturer]  # noqa: UP040
    CaliberAdminBase: TypeAlias = admin.ModelAdmin[Caliber]  # noqa: UP040
    FirearmModelAdminBase: TypeAlias = admin.ModelAdmin[FirearmModel]  # noqa: UP040
    CountryAdminBase: TypeAlias = admin.ModelAdmin[Country]  # noqa: UP040
    StateAdminBase: TypeAlias = admin.ModelAdmin[State]  # noqa: UP040
    CityAdminBase: TypeAlias = admin.ModelAdmin[City]  # noqa: UP040
    CaseTypeAdminBase: TypeAlias = admin.ModelAdmin[CaseType]  # noqa: UP040
    DocumentTypeAdminBase: TypeAlias = admin.ModelAdmin[DocumentType]  # noqa: UP040
    WorkflowTypeAdminBase: TypeAlias = admin.ModelAdmin[WorkflowType]  # noqa: UP040
    StatusTypeAdminBase: TypeAlias = admin.ModelAdmin[StatusType]  # noqa: UP040
else:
    ManufacturerAdminBase = admin.ModelAdmin
    CaliberAdminBase = admin.ModelAdmin
    FirearmModelAdminBase = admin.ModelAdmin
    CountryAdminBase = admin.ModelAdmin
    StateAdminBase = admin.ModelAdmin
    CityAdminBase = admin.ModelAdmin
    CaseTypeAdminBase = admin.ModelAdmin
    DocumentTypeAdminBase = admin.ModelAdmin
    WorkflowTypeAdminBase = admin.ModelAdmin
    StatusTypeAdminBase = admin.ModelAdmin


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


@admin.register(Country)
class CountryAdmin(CountryAdminBase):
    """Admin for countries."""

    list_display = ("name", "iso2", "iso3", "phone_code", "status")
    list_filter = ("status",)
    search_fields = ("name", "iso2", "iso3", "phone_code")
    readonly_fields = ("id", "created_at", "updated_at")


@admin.register(State)
class StateAdmin(StateAdminBase):
    """Admin for states."""

    list_display = ("name", "country", "code", "status")
    list_filter = ("status", "country")
    search_fields = ("name", "code", "country__name", "country__iso2")
    readonly_fields = ("id", "created_at", "updated_at")


@admin.register(City)
class CityAdmin(CityAdminBase):
    """Admin for cities."""

    list_display = ("name", "state", "ibge_code", "status")
    list_filter = ("status", "state__country", "state")
    search_fields = (
        "name",
        "ibge_code",
        "state__name",
        "state__country__name",
    )
    readonly_fields = ("id", "created_at", "updated_at")


@admin.register(CaseType)
class CaseTypeAdmin(CaseTypeAdminBase):
    """Admin for case type reference data."""

    list_display = ("name", "code", "is_system", "status", "created_at")
    list_filter = ("status", "is_system")
    search_fields = ("name", "code", "description")
    readonly_fields = ("id", "created_at", "updated_at")


@admin.register(DocumentType)
class DocumentTypeAdmin(DocumentTypeAdminBase):
    """Admin for document type reference data."""

    list_display = ("name", "code", "is_system", "status", "created_at")
    list_filter = ("status", "is_system")
    search_fields = ("name", "code", "description")
    readonly_fields = ("id", "created_at", "updated_at")


@admin.register(WorkflowType)
class WorkflowTypeAdmin(WorkflowTypeAdminBase):
    """Admin for workflow type reference data."""

    list_display = ("name", "code", "is_system", "status", "created_at")
    list_filter = ("status", "is_system")
    search_fields = ("name", "code", "description")
    readonly_fields = ("id", "created_at", "updated_at")


@admin.register(StatusType)
class StatusTypeAdmin(StatusTypeAdminBase):
    """Admin for status type reference data."""

    list_display = ("name", "code", "is_system", "status", "created_at")
    list_filter = ("status", "is_system")
    search_fields = ("name", "code", "description")
    readonly_fields = ("id", "created_at", "updated_at")
