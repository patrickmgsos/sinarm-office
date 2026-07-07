"""Tests for technical notification models."""

from __future__ import annotations

import uuid

import pytest
from django.contrib.auth import get_user_model
from django.db import IntegrityError

from apps.notification.models import (
    NotificationChannel,
    NotificationDelivery,
    NotificationMessage,
    NotificationTemplate,
)
from apps.organization.models import Organization

pytestmark = pytest.mark.django_db


def test_notification_channel_uses_uuid_and_supported_kind() -> None:
    """NotificationChannel should use UUID identity and supported kinds."""
    channel = NotificationChannel.objects.create(
        code="email-default",
        name="Email default",
        kind=NotificationChannel.ChannelKind.EMAIL,
    )

    assert isinstance(channel.id, uuid.UUID)
    assert channel.kind == NotificationChannel.ChannelKind.EMAIL


def test_notification_template_is_unique_per_scope_and_locale() -> None:
    """Templates should be unique by organization scope, code and locale."""
    organization = Organization.objects.create(name="SINARM Office")
    channel = NotificationChannel.objects.create(
        organization=organization,
        code="system",
        name="System",
        kind=NotificationChannel.ChannelKind.SYSTEM,
    )
    NotificationTemplate.objects.create(
        organization=organization,
        channel=channel,
        code="welcome",
        name="Welcome",
        body_template="Hello {name}",
    )

    with pytest.raises(IntegrityError):
        NotificationTemplate.objects.create(
            organization=organization,
            channel=channel,
            code="welcome",
            name="Duplicate",
            body_template="Hello again",
        )


def test_notification_message_records_recipient_and_status() -> None:
    """Messages should preserve recipient identity and queue status."""
    user_model = get_user_model()
    recipient = user_model.objects.create_user(username="notify-user")
    channel = NotificationChannel.objects.create(
        code="system",
        name="System",
        kind=NotificationChannel.ChannelKind.SYSTEM,
    )
    message = NotificationMessage.objects.create(
        channel=channel,
        recipient_user=recipient,
        body="Notification body",
    )

    assert message.recipient_user == recipient
    assert message.status == NotificationMessage.MessageStatus.PENDING


def test_notification_delivery_records_attempt_data() -> None:
    """Deliveries should keep provider attempt details."""
    channel = NotificationChannel.objects.create(
        code="email",
        name="Email",
        kind=NotificationChannel.ChannelKind.EMAIL,
    )
    message = NotificationMessage.objects.create(channel=channel, body="Body")
    delivery = NotificationDelivery.objects.create(
        message=message,
        attempt_number=1,
        provider="mail-provider",
        external_id="external-1",
        status=NotificationMessage.MessageStatus.FAILED,
        error_message="temporary failure",
    )

    assert delivery.message == message
    assert delivery.provider == "mail-provider"
    assert delivery.external_id == "external-1"
    assert delivery.error_message == "temporary failure"
