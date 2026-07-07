"""Tests for notification services."""

from __future__ import annotations

import pytest

from apps.common.models import ArchivableModel
from apps.notification.models import NotificationChannel, NotificationMessage
from apps.notification.services import (
    archive_notification_channel,
    archive_notification_template,
    cancel_notification_message,
    create_message_from_template,
    create_notification_channel,
    create_notification_message,
    create_notification_template,
    mark_notification_failed,
    mark_notification_sent,
    queue_notification_message,
    record_notification_delivery,
)

pytestmark = pytest.mark.django_db


def test_create_template_and_message_without_sending() -> None:
    """Services should model a pending message without real delivery."""
    channel = create_notification_channel(
        code="system",
        name="System",
        kind=NotificationChannel.ChannelKind.SYSTEM,
    )
    template = create_notification_template(
        channel=channel,
        code="welcome",
        name="Welcome",
        subject_template="Welcome {name}",
        body_template="Hello {name}",
    )
    message = create_message_from_template(
        template=template,
        context={"name": "Ada"},
    )

    assert message.subject == "Welcome Ada"
    assert message.body == "Hello Ada"
    assert message.status == NotificationMessage.MessageStatus.PENDING


def test_message_status_lifecycle_services() -> None:
    """Services should move messages through queue statuses."""
    channel = create_notification_channel(
        code="email",
        name="Email",
        kind=NotificationChannel.ChannelKind.EMAIL,
    )
    message = create_notification_message(channel=channel, body="Body")

    queue_notification_message(message)
    assert message.status == NotificationMessage.MessageStatus.QUEUED
    assert message.queued_at is not None

    mark_notification_sent(message)
    assert message.status == NotificationMessage.MessageStatus.SENT
    assert message.sent_at is not None

    failed = create_notification_message(channel=channel, body="Failure")
    mark_notification_failed(failed)
    assert failed.status == NotificationMessage.MessageStatus.FAILED
    assert failed.failed_at is not None

    cancelled = create_notification_message(channel=channel, body="Cancel")
    cancel_notification_message(cancelled)
    assert cancelled.status == NotificationMessage.MessageStatus.CANCELLED
    assert cancelled.cancelled_at is not None


def test_record_delivery_attempt_service() -> None:
    """Delivery service should record provider history only."""
    channel = create_notification_channel(
        code="sms",
        name="SMS",
        kind=NotificationChannel.ChannelKind.SMS,
    )
    message = create_notification_message(channel=channel, body="Body")
    delivery = record_notification_delivery(
        message=message,
        attempt_number=1,
        provider="sms-provider",
        external_id="sms-1",
        status=NotificationMessage.MessageStatus.FAILED,
        error_message="provider rejected",
        response_data={"code": "rejected"},
    )

    assert delivery.status == NotificationMessage.MessageStatus.FAILED
    assert delivery.failed_at is not None
    assert delivery.response_data == {"code": "rejected"}


def test_archive_channel_and_template_services() -> None:
    """Archive services should preserve notification history."""
    channel = create_notification_channel(
        code="whatsapp",
        name="WhatsApp",
        kind=NotificationChannel.ChannelKind.WHATSAPP,
    )
    template = create_notification_template(
        channel=channel,
        code="alert",
        name="Alert",
        body_template="Alert",
    )

    archive_notification_channel(channel)
    archive_notification_template(template)

    assert channel.status == ArchivableModel.ArchiveStatus.ARCHIVED
    assert template.status == ArchivableModel.ArchiveStatus.ARCHIVED
