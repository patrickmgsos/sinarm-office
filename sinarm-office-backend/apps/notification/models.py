"""Technical notification models for queueing and delivery history."""

from __future__ import annotations

from django.conf import settings
from django.db import models
from django.utils import timezone

from apps.common.models import ArchivableModel, BaseModel
from apps.organization.models import Organization


class NotificationChannel(BaseModel, ArchivableModel):
    """Configured notification channel for technical messaging."""

    class ChannelKind(models.TextChoices):
        EMAIL = "email", "Email"
        WHATSAPP = "whatsapp", "WhatsApp"
        SMS = "sms", "SMS"
        SYSTEM = "system", "System"

    organization = models.ForeignKey(
        Organization,
        blank=True,
        null=True,
        on_delete=models.PROTECT,
        related_name="notification_channels",
    )
    code = models.SlugField(max_length=120)
    name = models.CharField(max_length=180)
    kind = models.CharField(max_length=32, choices=ChannelKind.choices)
    provider = models.CharField(max_length=80, blank=True)
    metadata = models.JSONField(default=dict, blank=True)

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=["organization", "code"],
                name="ux_notification_channel_organization_code",
            ),
            models.UniqueConstraint(
                fields=["code"],
                condition=models.Q(organization__isnull=True),
                name="ux_notification_channel_global_code",
            ),
        ]
        ordering = ["code"]
        verbose_name = "notification channel"
        verbose_name_plural = "notification channels"

    def __str__(self) -> str:
        """Return the stable channel code."""
        return self.code


class NotificationTemplate(BaseModel, ArchivableModel):
    """Reusable technical notification template."""

    organization = models.ForeignKey(
        Organization,
        blank=True,
        null=True,
        on_delete=models.PROTECT,
        related_name="notification_templates",
    )
    channel = models.ForeignKey(
        NotificationChannel,
        on_delete=models.PROTECT,
        related_name="templates",
    )
    code = models.SlugField(max_length=140)
    name = models.CharField(max_length=180)
    subject_template = models.CharField(max_length=240, blank=True)
    body_template = models.TextField()
    locale = models.CharField(max_length=16, default="pt-br")
    metadata = models.JSONField(default=dict, blank=True)

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=["organization", "code", "locale"],
                name="ux_notification_template_organization_code_locale",
            ),
            models.UniqueConstraint(
                fields=["code", "locale"],
                condition=models.Q(organization__isnull=True),
                name="ux_notification_template_global_code_locale",
            ),
        ]
        ordering = ["code", "locale"]
        verbose_name = "notification template"
        verbose_name_plural = "notification templates"

    def __str__(self) -> str:
        """Return the stable template code."""
        return f"{self.code}:{self.locale}"


class NotificationMessage(BaseModel):
    """Queued technical notification message."""

    class MessageStatus(models.TextChoices):
        PENDING = "pending", "Pending"
        QUEUED = "queued", "Queued"
        SENT = "sent", "Sent"
        FAILED = "failed", "Failed"
        CANCELLED = "cancelled", "Cancelled"

    organization = models.ForeignKey(
        Organization,
        blank=True,
        null=True,
        on_delete=models.PROTECT,
        related_name="notification_messages",
    )
    channel = models.ForeignKey(
        NotificationChannel,
        on_delete=models.PROTECT,
        related_name="messages",
    )
    template = models.ForeignKey(
        NotificationTemplate,
        blank=True,
        null=True,
        on_delete=models.PROTECT,
        related_name="messages",
    )
    recipient_user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        blank=True,
        null=True,
        on_delete=models.SET_NULL,
        related_name="notification_messages",
    )
    recipient_address = models.CharField(max_length=240, blank=True)
    subject = models.CharField(max_length=240, blank=True)
    body = models.TextField()
    payload = models.JSONField(default=dict, blank=True)
    status = models.CharField(
        max_length=32,
        choices=MessageStatus.choices,
        default=MessageStatus.PENDING,
    )
    scheduled_at = models.DateTimeField(blank=True, null=True)
    queued_at = models.DateTimeField(blank=True, null=True)
    sent_at = models.DateTimeField(blank=True, null=True)
    failed_at = models.DateTimeField(blank=True, null=True)
    cancelled_at = models.DateTimeField(blank=True, null=True)
    metadata = models.JSONField(default=dict, blank=True)

    class Meta:
        indexes = [
            models.Index(fields=["status", "scheduled_at"]),
            models.Index(fields=["recipient_user", "created_at"]),
            models.Index(fields=["organization", "created_at"]),
            models.Index(fields=["channel", "status"]),
        ]
        ordering = ["-created_at"]
        verbose_name = "notification message"
        verbose_name_plural = "notification messages"

    def __str__(self) -> str:
        """Return a compact message label."""
        return f"{self.channel.code}:{self.status}:{self.id}"


class NotificationDelivery(BaseModel):
    """Provider delivery attempt for a notification message."""

    message = models.ForeignKey(
        NotificationMessage,
        on_delete=models.CASCADE,
        related_name="deliveries",
    )
    attempt_number = models.PositiveIntegerField()
    provider = models.CharField(max_length=80, blank=True)
    external_id = models.CharField(max_length=160, blank=True)
    status = models.CharField(
        max_length=32,
        choices=NotificationMessage.MessageStatus.choices,
        default=NotificationMessage.MessageStatus.PENDING,
    )
    error_message = models.TextField(blank=True)
    attempted_at = models.DateTimeField(default=timezone.now)
    queued_at = models.DateTimeField(blank=True, null=True)
    sent_at = models.DateTimeField(blank=True, null=True)
    failed_at = models.DateTimeField(blank=True, null=True)
    cancelled_at = models.DateTimeField(blank=True, null=True)
    response_data = models.JSONField(default=dict, blank=True)

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=["message", "attempt_number"],
                name="ux_notification_delivery_message_attempt",
            ),
        ]
        indexes = [
            models.Index(fields=["message", "attempt_number"]),
            models.Index(fields=["status", "attempted_at"]),
            models.Index(fields=["provider", "external_id"]),
        ]
        ordering = ["message", "attempt_number"]
        verbose_name = "notification delivery"
        verbose_name_plural = "notification deliveries"

    def __str__(self) -> str:
        """Return a compact delivery label."""
        return f"{self.message_id}:attempt:{self.attempt_number}"
