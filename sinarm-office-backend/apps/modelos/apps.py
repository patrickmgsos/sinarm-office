"""Modelos app configuration."""

from __future__ import annotations

from django.apps import AppConfig


class ModelosConfig(AppConfig):
    """Configuration for the modelos app."""

    default_auto_field = "django.db.models.BigAutoField"
    name = "apps.modelos"
