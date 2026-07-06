"""Technical audit models for platform-wide traceability."""

from __future__ import annotations

import uuid

from django.conf import settings
from django.db import models
from django.utils import timezone

from apps.common.models import BaseModel


class AuditEventType(BaseModel):
    """Catalog of auditable event types."""

    class Severity(models.TextChoices):
        INFO = "info", "Info"
        WARNING = "warning", "Warning"
        ERROR = "error", "Error"
        CRITICAL = "critical", "Critical"

    code = models.SlugField(max_length=120, unique=True)
    name = models.CharField(max_length=160)
    description = models.TextField(blank=True)
    severity = models.CharField(
        max_length=32,
        choices=Severity.choices,
        default=Severity.INFO,
    )
    is_active = models.BooleanField(default=True)

    class Meta:
        ordering = ["code"]
        verbose_name = "audit event type"
        verbose_name_plural = "audit event types"

    def __str__(self) -> str:
        """Return the stable event type code."""
        return self.code


class AuditSession(BaseModel):
    """Audit context for a user session or operational activity."""

    actor = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        blank=True,
        null=True,
        on_delete=models.SET_NULL,
        related_name="audit_sessions",
    )
    organization_id = models.UUIDField(blank=True, null=True, db_index=True)
    session_key = models.CharField(max_length=128, blank=True)
    ip_address = models.GenericIPAddressField(blank=True, null=True)
    user_agent = models.TextField(blank=True)
    auth_method = models.CharField(max_length=64, blank=True)
    started_at = models.DateTimeField(default=timezone.now)
    ended_at = models.DateTimeField(blank=True, null=True)
    metadata = models.JSONField(default=dict, blank=True)

    class Meta:
        indexes = [
            models.Index(fields=["actor", "started_at"]),
            models.Index(fields=["organization_id", "started_at"]),
        ]
        ordering = ["-started_at"]
        verbose_name = "audit session"
        verbose_name_plural = "audit sessions"

    def __str__(self) -> str:
        """Return a human-readable session label."""
        actor = self.actor_id or "anonymous"
        return f"audit-session:{actor}:{self.started_at.isoformat()}"


class AuditEvent(BaseModel):
    """Immutable audit event for important platform changes."""

    event_type = models.ForeignKey(
        AuditEventType,
        blank=True,
        null=True,
        on_delete=models.PROTECT,
        related_name="events",
    )
    audit_session = models.ForeignKey(
        AuditSession,
        blank=True,
        null=True,
        on_delete=models.SET_NULL,
        related_name="events",
    )
    actor = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        blank=True,
        null=True,
        on_delete=models.SET_NULL,
        related_name="audit_events",
    )
    organization_id = models.UUIDField(blank=True, null=True, db_index=True)
    action = models.CharField(max_length=120)
    entity_type = models.CharField(max_length=160)
    entity_id = models.UUIDField(blank=True, null=True, db_index=True)
    metadata = models.JSONField(default=dict, blank=True)
    before_data = models.JSONField(blank=True, null=True)
    after_data = models.JSONField(blank=True, null=True)
    ip_address = models.GenericIPAddressField(blank=True, null=True)
    user_agent = models.TextField(blank=True)
    occurred_at = models.DateTimeField(default=timezone.now)

    class Meta:
        indexes = [
            models.Index(fields=["entity_type", "entity_id"]),
            models.Index(fields=["actor", "occurred_at"]),
            models.Index(fields=["organization_id", "occurred_at"]),
            models.Index(fields=["action", "occurred_at"]),
        ]
        ordering = ["-occurred_at"]
        verbose_name = "audit event"
        verbose_name_plural = "audit events"

    def __str__(self) -> str:
        """Return a compact audit event representation."""
        return f"{self.action}:{self.entity_type}:{self.entity_id or 'none'}"


def new_entity_id() -> uuid.UUID:
    """Return a UUID for tests and service callers that need explicit IDs."""
    return uuid.uuid4()
