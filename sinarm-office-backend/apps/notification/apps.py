"""Notification app configuration."""

from __future__ import annotations

from django.apps import AppConfig


class NotificationConfig(AppConfig):
    """Configuration for notification infrastructure."""

    default_auto_field = "django.db.models.BigAutoField"
    name = "apps.notification"
