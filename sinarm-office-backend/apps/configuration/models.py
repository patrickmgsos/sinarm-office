"""Technical configuration models for runtime settings."""

from __future__ import annotations

from decimal import Decimal
from typing import Any, ClassVar

from django.core.exceptions import ValidationError
from django.db import models

from apps.common.models import ArchivableModel, BaseModel
from apps.organization.models import Organization


class SettingValueMixin(models.Model):
    """Typed value storage shared by configuration settings."""

    class ValueType(models.TextChoices):
        STRING = "string", "String"
        BOOLEAN = "boolean", "Boolean"
        INTEGER = "integer", "Integer"
        DECIMAL = "decimal", "Decimal"
        JSON = "json", "JSON"

    SECRET_KEY_FRAGMENTS: ClassVar[tuple[str, ...]] = (
        "api_key",
        "credential",
        "password",
        "private_key",
        "secret",
        "token",
    )

    value_type = models.CharField(max_length=32, choices=ValueType.choices)
    string_value = models.TextField(blank=True)
    boolean_value = models.BooleanField(blank=True, null=True)
    integer_value = models.IntegerField(blank=True, null=True)
    decimal_value = models.DecimalField(
        blank=True,
        null=True,
        max_digits=18,
        decimal_places=6,
    )
    json_value = models.JSONField(blank=True, null=True)

    class Meta:
        abstract = True

    def clean(self) -> None:
        """Validate that the configured key is not intended for secrets."""
        super().clean()
        key = str(getattr(self, "key", "")).lower()
        if any(fragment in key for fragment in self.SECRET_KEY_FRAGMENTS):
            msg = "Sensitive secrets must not be stored in configuration settings."
            raise ValidationError({"key": msg})

    def get_value(self) -> str | bool | int | Decimal | Any | None:
        """Return the active typed value."""
        if self.value_type == self.ValueType.STRING:
            return self.string_value
        if self.value_type == self.ValueType.BOOLEAN:
            return self.boolean_value
        if self.value_type == self.ValueType.INTEGER:
            return self.integer_value
        if self.value_type == self.ValueType.DECIMAL:
            return self.decimal_value
        if self.value_type == self.ValueType.JSON:
            return self.json_value

        return None

    def set_value(self, value: str | bool | int | Decimal | dict[str, Any]) -> None:
        """Set the typed value and clear other storage columns."""
        self.string_value = ""
        self.boolean_value = None
        self.integer_value = None
        self.decimal_value = None
        self.json_value = None

        if isinstance(value, bool):
            self.value_type = self.ValueType.BOOLEAN
            self.boolean_value = value
        elif isinstance(value, int):
            self.value_type = self.ValueType.INTEGER
            self.integer_value = value
        elif isinstance(value, Decimal):
            self.value_type = self.ValueType.DECIMAL
            self.decimal_value = value
        elif isinstance(value, dict):
            self.value_type = self.ValueType.JSON
            self.json_value = value
        else:
            self.value_type = self.ValueType.STRING
            self.string_value = value


class SystemSetting(BaseModel, ArchivableModel, SettingValueMixin):
    """Platform-wide technical setting."""

    key = models.SlugField(max_length=140, unique=True)
    name = models.CharField(max_length=180)
    description = models.TextField(blank=True)

    class Meta:
        ordering = ["key"]
        verbose_name = "system setting"
        verbose_name_plural = "system settings"

    def __str__(self) -> str:
        """Return the stable setting key."""
        return self.key


class OrganizationSetting(BaseModel, ArchivableModel, SettingValueMixin):
    """Organization-scoped technical setting."""

    organization = models.ForeignKey(
        Organization,
        on_delete=models.PROTECT,
        related_name="settings",
    )
    key = models.SlugField(max_length=140)
    name = models.CharField(max_length=180)
    description = models.TextField(blank=True)

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=["organization", "key"],
                name="ux_configuration_organization_key",
            ),
        ]
        ordering = ["organization__name", "key"]
        verbose_name = "organization setting"
        verbose_name_plural = "organization settings"

    def __str__(self) -> str:
        """Return a scoped setting label."""
        return f"{self.organization_id}:{self.key}"
