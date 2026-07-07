"""Application services for technical notification queue records."""

from __future__ import annotations

from collections.abc import Mapping
from typing import Any

from django.db import transaction
from django.utils import timezone

from apps.common.models import ArchivableModel
from apps.identity.models import CustomUser
from apps.notification.models import (
    NotificationChannel,
    NotificationDelivery,
    NotificationMessage,
    NotificationTemplate,
)
from apps.organization.models import Organization


def _render_template(template: str, context: Mapping[str, Any]) -> str:
    """Render a simple technical template using format placeholders."""
    return template.format(**context)


@transaction.atomic
def create_notification_channel(
    *,
    code: str,
    name: str,
    kind: str,
    organization: Organization | None = None,
    provider: str = "",
    metadata: Mapping[str, Any] | None = None,
) -> NotificationChannel:
    """Create a notification channel configuration."""
    return NotificationChannel.objects.create(
        organization=organization,
        code=code,
        name=name,
        kind=kind,
        provider=provider,
        metadata=dict(metadata or {}),
    )


@transaction.atomic
def create_notification_template(
    *,
    channel: NotificationChannel,
    code: str,
    name: str,
    body_template: str,
    organization: Organization | None = None,
    subject_template: str = "",
    locale: str = "pt-br",
    metadata: Mapping[str, Any] | None = None,
) -> NotificationTemplate:
    """Create a reusable notification template."""
    return NotificationTemplate.objects.create(
        organization=organization,
        channel=channel,
        code=code,
        name=name,
        subject_template=subject_template,
        body_template=body_template,
        locale=locale,
        metadata=dict(metadata or {}),
    )


@transaction.atomic
def create_notification_message(
    *,
    channel: NotificationChannel,
    body: str,
    organization: Organization | None = None,
    template: NotificationTemplate | None = None,
    recipient_user: CustomUser | None = None,
    recipient_address: str = "",
    subject: str = "",
    payload: Mapping[str, Any] | None = None,
    scheduled_at: Any | None = None,
    metadata: Mapping[str, Any] | None = None,
) -> NotificationMessage:
    """Create a pending notification message without sending it."""
    return NotificationMessage.objects.create(
        organization=organization,
        channel=channel,
        template=template,
        recipient_user=recipient_user,
        recipient_address=recipient_address,
        subject=subject,
        body=body,
        payload=dict(payload or {}),
        scheduled_at=scheduled_at,
        metadata=dict(metadata or {}),
    )


@transaction.atomic
def create_message_from_template(
    *,
    template: NotificationTemplate,
    context: Mapping[str, Any],
    organization: Organization | None = None,
    recipient_user: CustomUser | None = None,
    recipient_address: str = "",
    scheduled_at: Any | None = None,
    metadata: Mapping[str, Any] | None = None,
) -> NotificationMessage:
    """Create a pending notification message from a stored template."""
    return create_notification_message(
        organization=organization or template.organization,
        channel=template.channel,
        template=template,
        recipient_user=recipient_user,
        recipient_address=recipient_address,
        subject=_render_template(template.subject_template, context),
        body=_render_template(template.body_template, context),
        payload=dict(context),
        scheduled_at=scheduled_at,
        metadata=metadata,
    )


@transaction.atomic
def queue_notification_message(
    message: NotificationMessage,
) -> NotificationMessage:
    """Mark a notification message as queued for later delivery."""
    message.status = NotificationMessage.MessageStatus.QUEUED
    message.queued_at = timezone.now()
    message.save(update_fields=["status", "queued_at", "updated_at"])
    return message


@transaction.atomic
def mark_notification_sent(message: NotificationMessage) -> NotificationMessage:
    """Mark a notification message as sent."""
    message.status = NotificationMessage.MessageStatus.SENT
    message.sent_at = timezone.now()
    message.save(update_fields=["status", "sent_at", "updated_at"])
    return message


@transaction.atomic
def mark_notification_failed(message: NotificationMessage) -> NotificationMessage:
    """Mark a notification message as failed."""
    message.status = NotificationMessage.MessageStatus.FAILED
    message.failed_at = timezone.now()
    message.save(update_fields=["status", "failed_at", "updated_at"])
    return message


@transaction.atomic
def cancel_notification_message(message: NotificationMessage) -> NotificationMessage:
    """Cancel a pending or queued notification message."""
    message.status = NotificationMessage.MessageStatus.CANCELLED
    message.cancelled_at = timezone.now()
    message.save(update_fields=["status", "cancelled_at", "updated_at"])
    return message


@transaction.atomic
def record_notification_delivery(
    *,
    message: NotificationMessage,
    attempt_number: int,
    status: str,
    provider: str = "",
    external_id: str = "",
    error_message: str = "",
    response_data: Mapping[str, Any] | None = None,
) -> NotificationDelivery:
    """Record a provider delivery attempt without sending anything."""
    now = timezone.now()
    delivery = NotificationDelivery(
        message=message,
        attempt_number=attempt_number,
        provider=provider,
        external_id=external_id,
        status=status,
        error_message=error_message,
        response_data=dict(response_data or {}),
    )
    if status == NotificationMessage.MessageStatus.QUEUED:
        delivery.queued_at = now
    elif status == NotificationMessage.MessageStatus.SENT:
        delivery.sent_at = now
    elif status == NotificationMessage.MessageStatus.FAILED:
        delivery.failed_at = now
    elif status == NotificationMessage.MessageStatus.CANCELLED:
        delivery.cancelled_at = now

    delivery.save()
    return delivery


@transaction.atomic
def archive_notification_channel(
    channel: NotificationChannel,
) -> NotificationChannel:
    """Archive a channel without deleting historical notification records."""
    channel.status = ArchivableModel.ArchiveStatus.ARCHIVED
    channel.archived_at = timezone.now()
    channel.save(update_fields=["status", "archived_at", "updated_at"])
    return channel


@transaction.atomic
def archive_notification_template(
    template: NotificationTemplate,
) -> NotificationTemplate:
    """Archive a template without deleting historical notification records."""
    template.status = ArchivableModel.ArchiveStatus.ARCHIVED
    template.archived_at = timezone.now()
    template.save(update_fields=["status", "archived_at", "updated_at"])
    return template
