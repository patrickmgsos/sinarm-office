"""Workflows app configuration."""

from __future__ import annotations

from django.apps import AppConfig


class WorkflowsConfig(AppConfig):
    """Configuration for the workflows app."""

    default_auto_field = "django.db.models.BigAutoField"
    name = "apps.workflows"
