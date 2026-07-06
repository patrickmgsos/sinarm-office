"""Reusable abstract model mixins."""

from __future__ import annotations

import uuid

from django.conf import settings
from django.db import models


class UUIDModel(models.Model):
    """Abstract model with UUID primary key identity."""

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)

    class Meta:
        abstract = True


class TimestampedModel(models.Model):
    """Abstract model with creation and update timestamps."""

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class UserStampedModel(models.Model):
    """Abstract model with optional actor references for audit metadata."""

    created_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        blank=True,
        null=True,
        on_delete=models.SET_NULL,
        related_name="%(app_label)s_%(class)s_created",
    )
    updated_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        blank=True,
        null=True,
        on_delete=models.SET_NULL,
        related_name="%(app_label)s_%(class)s_updated",
    )

    class Meta:
        abstract = True


class BaseModel(UUIDModel, TimestampedModel, UserStampedModel):
    """Base model for future persistent entities."""

    class Meta:
        abstract = True


class ArchivableModel(models.Model):
    """Abstract mixin for entities that support juridical archiving."""

    class ArchiveStatus(models.TextChoices):
        ACTIVE = "active", "Active"
        INACTIVE = "inactive", "Inactive"
        ARCHIVED = "archived", "Archived"
        CANCELLED = "cancelled", "Cancelled"

    status = models.CharField(
        max_length=32,
        choices=ArchiveStatus.choices,
        default=ArchiveStatus.ACTIVE,
    )
    archived_at = models.DateTimeField(blank=True, null=True)
    archived_by = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        blank=True,
        null=True,
        on_delete=models.SET_NULL,
        related_name="%(app_label)s_%(class)s_archived",
    )

    class Meta:
        abstract = True
