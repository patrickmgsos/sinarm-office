"""Document generation MVP app configuration."""

from __future__ import annotations

from django.apps import AppConfig


class DocumentsConfig(AppConfig):
    """Configuration for the Document generation MVP."""

    default_auto_field = "django.db.models.BigAutoField"
    name = "apps.documents"
    verbose_name = "Documents"
