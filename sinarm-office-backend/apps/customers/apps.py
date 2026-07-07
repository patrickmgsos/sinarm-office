"""Customer domain app configuration."""

from __future__ import annotations

from django.apps import AppConfig


class CustomersConfig(AppConfig):
    """Configuration for the Customer Domain."""

    default_auto_field = "django.db.models.BigAutoField"
    name = "apps.customers"
