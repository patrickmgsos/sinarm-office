"""Django admin configuration for Customer Domain."""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeAlias

from django.contrib import admin

from apps.customers.models import Customer, CustomerAddress, CustomerContact

if TYPE_CHECKING:
    CustomerAdminBase: TypeAlias = admin.ModelAdmin[Customer]  # noqa: UP040
    CustomerAddressInlineBase: TypeAlias = admin.TabularInline[  # noqa: UP040
        CustomerAddress, Customer
    ]
    CustomerAddressAdminBase: TypeAlias = admin.ModelAdmin[CustomerAddress]  # noqa: UP040
    CustomerContactInlineBase: TypeAlias = admin.TabularInline[  # noqa: UP040
        CustomerContact, Customer
    ]
    CustomerContactAdminBase: TypeAlias = admin.ModelAdmin[CustomerContact]  # noqa: UP040
else:
    CustomerAdminBase = admin.ModelAdmin
    CustomerAddressInlineBase = admin.TabularInline
    CustomerAddressAdminBase = admin.ModelAdmin
    CustomerContactInlineBase = admin.TabularInline
    CustomerContactAdminBase = admin.ModelAdmin


class CustomerAddressInline(CustomerAddressInlineBase):
    """Inline admin for customer addresses."""

    model = CustomerAddress
    extra = 0
    fields = (
        "address_type",
        "street",
        "number",
        "district",
        "city",
        "state",
        "country",
        "is_primary",
        "status",
    )
    readonly_fields = ("id",)


class CustomerContactInline(CustomerContactInlineBase):
    """Inline admin for customer contacts."""

    model = CustomerContact
    extra = 0
    fields = ("contact_type", "value", "label", "is_primary", "status")
    readonly_fields = ("id",)


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
    inlines = [CustomerAddressInline, CustomerContactInline]


@admin.register(CustomerAddress)
class CustomerAddressAdmin(CustomerAddressAdminBase):
    """Admin for customer addresses."""

    list_display = (
        "customer",
        "address_type",
        "street",
        "city",
        "state",
        "is_primary",
        "status",
    )
    list_filter = ("status", "address_type", "is_primary", "country", "state")
    search_fields = ("customer__name", "street", "district", "postal_code")
    readonly_fields = ("id", "created_at", "updated_at")


@admin.register(CustomerContact)
class CustomerContactAdmin(CustomerContactAdminBase):
    """Admin for customer contacts."""

    list_display = (
        "customer",
        "contact_type",
        "value",
        "label",
        "is_primary",
        "status",
    )
    list_filter = ("status", "contact_type", "is_primary")
    search_fields = ("customer__name", "value", "label")
    readonly_fields = ("id", "created_at", "updated_at")
