"""Firearm MVP models."""

from __future__ import annotations

from django.db import models

from apps.common.models import ArchivableModel, BaseModel
from apps.customers.models import Customer
from apps.reference_data.models import Caliber, FirearmModel, Manufacturer


def craf_upload_to(instance: Firearm, filename: str) -> str:
    """Return upload path for CRAF files."""
    return f"firearms/{instance.customer_id}/craf/{filename}"


class Firearm(BaseModel, ArchivableModel):
    """Operational firearm record for the MVP."""

    customer = models.ForeignKey(
        Customer,
        on_delete=models.PROTECT,
        related_name="firearms",
    )
    manufacturer = models.ForeignKey(
        Manufacturer,
        blank=True,
        null=True,
        on_delete=models.PROTECT,
        related_name="operational_firearms",
    )
    model = models.ForeignKey(
        FirearmModel,
        blank=True,
        null=True,
        on_delete=models.PROTECT,
        related_name="operational_firearms",
    )
    caliber = models.ForeignKey(
        Caliber,
        blank=True,
        null=True,
        on_delete=models.PROTECT,
        related_name="operational_firearms",
    )
    serial_number = models.CharField(max_length=120, db_index=True)
    sinarm_registration = models.CharField(max_length=120, blank=True, db_index=True)
    registration_valid_until = models.DateField(blank=True, null=True)
    craf_file = models.FileField(blank=True, upload_to=craf_upload_to)
    notes = models.TextField(blank=True)

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=["serial_number"],
                name="ux_firearm_serial_number",
            ),
        ]
        indexes = [
            models.Index(fields=["customer", "status"]),
            models.Index(fields=["registration_valid_until"]),
        ]
        ordering = ["customer__name", "serial_number"]
        verbose_name = "firearm"
        verbose_name_plural = "firearms"

    def __str__(self) -> str:
        """Return firearm display label."""
        return f"{self.customer.name} - {self.serial_number}"
