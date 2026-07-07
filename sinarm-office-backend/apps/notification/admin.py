"""Django admin configuration for notification models."""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeAlias

from django.contrib import admin

from apps.notification.models import (
    NotificationChannel,
    NotificationDelivery,
    NotificationMessage,
    NotificationTemplate,
)

if TYPE_CHECKING:
    # fmt: off
    NotificationChannelAdminBase: TypeAlias = (  # noqa: UP040
        admin.ModelAdmin[NotificationChannel]
    )
    NotificationTemplateAdminBase: TypeAlias = (  # noqa: UP040
        admin.ModelAdmin[NotificationTemplate]
    )
    NotificationMessageAdminBase: TypeAlias = (  # noqa: UP040
        admin.ModelAdmin[NotificationMessage]
    )
    NotificationDeliveryAdminBase: TypeAlias = (  # noqa: UP040
        admin.ModelAdmin[NotificationDelivery]
    )
    # fmt: on
else:
    NotificationChannelAdminBase = admin.ModelAdmin
    NotificationTemplateAdminBase = admin.ModelAdmin
    NotificationMessageAdminBase = admin.ModelAdmin
    NotificationDeliveryAdminBase = admin.ModelAdmin


@admin.register(NotificationChannel)
class NotificationChannelAdmin(NotificationChannelAdminBase):
    """Admin for notification channels."""

    list_display = ("code", "name", "kind", "provider", "organization", "status")
    list_filter = ("kind", "status", "organization")
    search_fields = ("code", "name", "provider", "organization__name")
    readonly_fields = ("id", "created_at", "updated_at")


@admin.register(NotificationTemplate)
class NotificationTemplateAdmin(NotificationTemplateAdminBase):
    """Admin for notification templates."""

    list_display = ("code", "name", "channel", "locale", "organization", "status")
    list_filter = ("status", "locale", "channel", "organization")
    search_fields = ("code", "name", "subject_template", "body_template")
    readonly_fields = ("id", "created_at", "updated_at")


@admin.register(NotificationMessage)
class NotificationMessageAdmin(NotificationMessageAdminBase):
    """Admin for queued notification messages."""

    list_display = (
        "id",
        "channel",
        "recipient_user",
        "recipient_address",
        "status",
        "created_at",
    )
    list_filter = ("status", "channel", "organization")
    search_fields = ("recipient_address", "subject", "body")
    readonly_fields = (
        "id",
        "created_at",
        "updated_at",
        "queued_at",
        "sent_at",
        "failed_at",
        "cancelled_at",
    )


@admin.register(NotificationDelivery)
class NotificationDeliveryAdmin(NotificationDeliveryAdminBase):
    """Admin for notification delivery attempts."""

    list_display = (
        "message",
        "attempt_number",
        "provider",
        "external_id",
        "status",
        "attempted_at",
    )
    list_filter = ("status", "provider")
    search_fields = ("external_id", "error_message", "message__recipient_address")
    readonly_fields = ("id", "created_at", "updated_at", "attempted_at")
