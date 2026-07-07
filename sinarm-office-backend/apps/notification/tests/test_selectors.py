"""Tests for notification selectors."""

from __future__ import annotations

import pytest
from django.contrib.auth import get_user_model

from apps.common.models import ArchivableModel
from apps.notification.models import NotificationChannel, NotificationMessage
from apps.notification.selectors import (
    notification_channels_active,
    notification_deliveries_for_message,
    notification_messages_by_status,
    notification_messages_for_user,
    notification_templates_active,
)
from apps.notification.services import (
    create_notification_channel,
    create_notification_message,
    create_notification_template,
    record_notification_delivery,
)
from apps.organization.models import Organization

pytestmark = pytest.mark.django_db


def test_active_channel_and_template_selectors_filter_scope() -> None:
    """Selectors should return active global and scoped records."""
    organization = Organization.objects.create(name="SINARM Office")
    global_channel = create_notification_channel(
        code="global-system",
        name="Global system",
        kind=NotificationChannel.ChannelKind.SYSTEM,
    )
    scoped_channel = create_notification_channel(
        organization=organization,
        code="scoped-email",
        name="Scoped email",
        kind=NotificationChannel.ChannelKind.EMAIL,
    )
    archived = create_notification_channel(
        code="archived",
        name="Archived",
        kind=NotificationChannel.ChannelKind.SMS,
    )
    archived.status = ArchivableModel.ArchiveStatus.ARCHIVED
    archived.save(update_fields=["status"])
    global_template = create_notification_template(
        channel=global_channel,
        code="global-template",
        name="Global template",
        body_template="Global",
    )
    scoped_template = create_notification_template(
        organization=organization,
        channel=scoped_channel,
        code="scoped-template",
        name="Scoped template",
        body_template="Scoped",
    )

    assert list(notification_channels_active(organization_id=organization.id)) == [
        global_channel,
        scoped_channel,
    ]
    assert list(notification_templates_active(organization_id=organization.id)) == [
        global_template,
        scoped_template,
    ]


def test_message_selectors_filter_status_and_user() -> None:
    """Message selectors should filter status and recipient user."""
    user_model = get_user_model()
    recipient = user_model.objects.create_user(username="recipient")
    other = user_model.objects.create_user(username="other")
    channel = create_notification_channel(
        code="system",
        name="System",
        kind=NotificationChannel.ChannelKind.SYSTEM,
    )
    expected = create_notification_message(
        channel=channel,
        recipient_user=recipient,
        body="Expected",
    )
    expected.status = NotificationMessage.MessageStatus.QUEUED
    expected.save(update_fields=["status"])
    create_notification_message(channel=channel, recipient_user=other, body="Other")

    assert list(
        notification_messages_by_status(
            status=NotificationMessage.MessageStatus.QUEUED,
        ),
    ) == [expected]
    assert list(notification_messages_for_user(user_id=recipient.id)) == [expected]


def test_deliveries_for_message_selector() -> None:
    """Delivery selector should return attempts for one message."""
    channel = create_notification_channel(
        code="email",
        name="Email",
        kind=NotificationChannel.ChannelKind.EMAIL,
    )
    message = create_notification_message(channel=channel, body="Body")
    other = create_notification_message(channel=channel, body="Other")
    expected = record_notification_delivery(
        message=message,
        attempt_number=1,
        status=NotificationMessage.MessageStatus.SENT,
        provider="mail-provider",
        external_id="external-1",
    )
    record_notification_delivery(
        message=other,
        attempt_number=1,
        status=NotificationMessage.MessageStatus.SENT,
    )

    assert list(notification_deliveries_for_message(message_id=message.id)) == [
        expected
    ]
