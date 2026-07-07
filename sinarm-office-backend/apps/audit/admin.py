"""Django admin configuration for technical audit models."""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeAlias

from django.contrib import admin

from apps.audit.models import AuditEvent, AuditEventType, AuditSession

if TYPE_CHECKING:
    EventTypeAdmin: TypeAlias = admin.ModelAdmin[AuditEventType]  # noqa: UP040
    SessionAdmin: TypeAlias = admin.ModelAdmin[AuditSession]  # noqa: UP040
    EventAdmin: TypeAlias = admin.ModelAdmin[AuditEvent]  # noqa: UP040
else:
    EventTypeAdmin = admin.ModelAdmin
    SessionAdmin = admin.ModelAdmin
    EventAdmin = admin.ModelAdmin


@admin.register(AuditEventType)
class AuditEventTypeAdmin(EventTypeAdmin):
    """Admin for audit event type catalog."""

    list_display = ("code", "name", "severity", "is_active", "created_at")
    list_filter = ("severity", "is_active")
    search_fields = ("code", "name", "description")
    readonly_fields = ("id", "created_at", "updated_at")


@admin.register(AuditSession)
class AuditSessionAdmin(SessionAdmin):
    """Admin for audit sessions."""

    list_display = ("id", "actor", "organization_id", "ip_address", "started_at")
    list_filter = ("started_at", "ended_at")
    search_fields = ("session_key", "user_agent", "auth_method")
    readonly_fields = ("id", "created_at", "updated_at")


@admin.register(AuditEvent)
class AuditEventAdmin(EventAdmin):
    """Admin for audit events."""

    list_display = (
        "action",
        "entity_type",
        "entity_id",
        "actor",
        "organization_id",
        "occurred_at",
    )
    list_filter = ("action", "entity_type", "occurred_at")
    search_fields = ("action", "entity_type", "user_agent")
    readonly_fields = ("id", "created_at", "updated_at")
