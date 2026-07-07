"""Firearm MVP app configuration."""

from __future__ import annotations

from django.apps import AppConfig


class FirearmsConfig(AppConfig):
    """Configuration for the Firearm MVP domain."""

    default_auto_field = "django.db.models.BigAutoField"
    name = "apps.firearms"
    verbose_name = "Firearms"
