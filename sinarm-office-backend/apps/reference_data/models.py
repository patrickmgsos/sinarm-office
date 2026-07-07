"""Technical reference data for firearms without firearm ownership records."""

from __future__ import annotations

from django.db import models

from apps.common.models import ArchivableModel, BaseModel


class Manufacturer(BaseModel, ArchivableModel):
    """Firearm manufacturer reference data."""

    name = models.CharField(max_length=180, unique=True)
    country = models.CharField(max_length=120, blank=True)
    notes = models.TextField(blank=True)

    class Meta:
        ordering = ["name"]
        verbose_name = "manufacturer"
        verbose_name_plural = "manufacturers"

    def __str__(self) -> str:
        """Return manufacturer display name."""
        return self.name


class Caliber(BaseModel, ArchivableModel):
    """Caliber reference data."""

    name = models.CharField(max_length=120, unique=True)
    category = models.CharField(max_length=120, blank=True)
    description = models.TextField(blank=True)

    class Meta:
        ordering = ["name"]
        verbose_name = "caliber"
        verbose_name_plural = "calibers"

    def __str__(self) -> str:
        """Return caliber display name."""
        return self.name


class FirearmModel(BaseModel, ArchivableModel):
    """Firearm model reference data without creating Firearm entities."""

    manufacturer = models.ForeignKey(
        Manufacturer,
        on_delete=models.PROTECT,
        related_name="firearm_models",
    )
    name = models.CharField(max_length=180)
    caliber = models.ForeignKey(
        Caliber,
        blank=True,
        null=True,
        on_delete=models.PROTECT,
        related_name="firearm_models",
    )
    species = models.CharField(max_length=120, blank=True)
    operation = models.CharField(max_length=120, blank=True)
    notes = models.TextField(blank=True)

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=["manufacturer", "name"],
                name="ux_reference_firearm_model_manufacturer_name",
            ),
        ]
        ordering = ["manufacturer__name", "name"]
        verbose_name = "firearm model"
        verbose_name_plural = "firearm models"

    def __str__(self) -> str:
        """Return firearm model display name."""
        return f"{self.manufacturer.name} - {self.name}"
