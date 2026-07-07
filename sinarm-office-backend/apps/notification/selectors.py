"""Query helpers for technical notification records."""

from __future__ import annotations

import uuid

from django.db.models import Q, QuerySet

from apps.common.models import ArchivableModel
from apps.notification.models import (
    NotificationChannel,
    NotificationDelivery,
    NotificationMessage,
    NotificationTemplate,
)


def notification_channels_active(
    *,
    organization_id: uuid.UUID | None = None,
    include_global: bool = True,
) -> QuerySet[NotificationChannel]:
    """Return active notification channels for an optional scope."""
    queryset = NotificationChannel.objects.filter(
        status=ArchivableModel.ArchiveStatus.ACTIVE,
    )
    if organization_id is not None and include_global:
        queryset = queryset.filter(
            Q(organization_id=organization_id) | Q(organization_id__isnull=True),
        )
    elif organization_id is not None:
        queryset = queryset.filter(organization_id=organization_id)
    else:
        queryset = queryset.filter(organization_id__isnull=True)

    return queryset.order_by("code")


def notification_templates_active(
    *,
    organization_id: uuid.UUID | None = None,
    include_global: bool = True,
) -> QuerySet[NotificationTemplate]:
    """Return active notification templates for an optional scope."""
    queryset = NotificationTemplate.objects.filter(
        status=ArchivableModel.ArchiveStatus.ACTIVE,
    ).select_related("channel", "organization")
    if organization_id is not None and include_global:
        queryset = queryset.filter(
            Q(organization_id=organization_id) | Q(organization_id__isnull=True),
        )
    elif organization_id is not None:
        queryset = queryset.filter(organization_id=organization_id)
    else:
        queryset = queryset.filter(organization_id__isnull=True)

    return queryset.order_by("code", "locale")


def notification_messages_by_status(
    *,
    status: str,
) -> QuerySet[NotificationMessage]:
    """Return notification messages by status."""
    return NotificationMessage.objects.filter(status=status).select_related(
        "channel",
        "template",
        "recipient_user",
        "organization",
    )


def notification_messages_for_user(
    *,
    user_id: uuid.UUID,
) -> QuerySet[NotificationMessage]:
    """Return notification messages addressed to a user."""
    return NotificationMessage.objects.filter(recipient_user_id=user_id).select_related(
        "channel",
        "template",
        "organization",
    )


def notification_deliveries_for_message(
    *,
    message_id: uuid.UUID,
) -> QuerySet[NotificationDelivery]:
    """Return delivery attempts for a message."""
    return NotificationDelivery.objects.filter(message_id=message_id).select_related(
        "message",
    )
