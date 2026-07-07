"""Django admin configuration for identity models."""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeAlias

from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from apps.identity.models import CustomUser, Permission, Role, UserRole, UserSession

if TYPE_CHECKING:
    CustomUserAdminBase: TypeAlias = UserAdmin[CustomUser]  # noqa: UP040
    PermissionAdminBase: TypeAlias = admin.ModelAdmin[Permission]  # noqa: UP040
    RoleAdminBase: TypeAlias = admin.ModelAdmin[Role]  # noqa: UP040
    UserRoleAdminBase: TypeAlias = admin.ModelAdmin[UserRole]  # noqa: UP040
    UserSessionAdminBase: TypeAlias = admin.ModelAdmin[UserSession]  # noqa: UP040
else:
    CustomUserAdminBase = UserAdmin
    PermissionAdminBase = admin.ModelAdmin
    RoleAdminBase = admin.ModelAdmin
    UserRoleAdminBase = admin.ModelAdmin
    UserSessionAdminBase = admin.ModelAdmin


@admin.register(CustomUser)
class CustomUserAdmin(CustomUserAdminBase):
    """Admin for custom users."""

    base_fieldsets = UserAdmin.fieldsets or ()
    base_add_fieldsets = UserAdmin.add_fieldsets or ()
    list_display = (
        "username",
        "email",
        "display_name",
        "organization_id",
        "is_active",
        "is_staff",
    )
    list_filter = ("is_active", "is_staff", "is_superuser")
    search_fields = ("username", "email", "display_name", "first_name", "last_name")
    readonly_fields = ("id", "created_at", "updated_at", "last_login", "date_joined")
    fieldsets = (
        *base_fieldsets,
        (
            "Technical identity",
            {
                "fields": (
                    "display_name",
                    "organization_id",
                    "timezone",
                    "locale",
                    "last_seen_at",
                    "created_by",
                    "updated_by",
                    "created_at",
                    "updated_at",
                ),
            },
        ),
    )
    add_fieldsets = (
        *base_add_fieldsets,
        (
            "Technical identity",
            {
                "fields": (
                    "email",
                    "display_name",
                    "organization_id",
                    "timezone",
                    "locale",
                ),
            },
        ),
    )


@admin.register(Permission)
class PermissionAdmin(PermissionAdminBase):
    """Admin for technical permissions."""

    list_display = ("code", "name", "is_active", "created_at")
    list_filter = ("is_active",)
    search_fields = ("code", "name", "description")
    readonly_fields = ("id", "created_at", "updated_at")


@admin.register(Role)
class RoleAdmin(RoleAdminBase):
    """Admin for technical roles."""

    list_display = ("code", "name", "organization_id", "status", "created_at")
    list_filter = ("status",)
    search_fields = ("code", "name", "description")
    readonly_fields = ("id", "created_at", "updated_at")
    filter_horizontal = ("permissions",)


@admin.register(UserRole)
class UserRoleAdmin(UserRoleAdminBase):
    """Admin for user role assignments."""

    list_display = ("user", "role", "organization_id", "status", "assigned_at")
    list_filter = ("status", "role")
    search_fields = ("user__username", "user__email", "role__code", "role__name")
    readonly_fields = ("id", "created_at", "updated_at", "assigned_at")


@admin.register(UserSession)
class UserSessionAdmin(UserSessionAdminBase):
    """Admin for user session metadata."""

    list_display = ("user", "session_key", "status", "started_at", "ended_at")
    list_filter = ("status", "auth_method")
    search_fields = ("user__username", "user__email", "session_key", "ip_address")
    readonly_fields = ("id", "created_at", "updated_at", "started_at")
