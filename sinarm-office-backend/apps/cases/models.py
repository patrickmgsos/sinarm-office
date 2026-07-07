"""Case MVP models."""

from __future__ import annotations

from django.conf import settings
from django.db import models
from django.utils import timezone

from apps.common.models import ArchivableModel, BaseModel
from apps.customers.models import Customer
from apps.reference_data.models import CaseType, StatusType


class Case(BaseModel, ArchivableModel):
    """Operational case record for the MVP."""

    customer = models.ForeignKey(
        Customer,
        on_delete=models.PROTECT,
        related_name="cases",
    )
    case_type = models.ForeignKey(
        CaseType,
        blank=True,
        null=True,
        on_delete=models.PROTECT,
        related_name="operational_cases",
    )
    status_type = models.ForeignKey(
        StatusType,
        blank=True,
        null=True,
        on_delete=models.PROTECT,
        related_name="operational_cases",
    )
    responsible_user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        blank=True,
        null=True,
        on_delete=models.SET_NULL,
        related_name="responsible_cases",
    )
    opened_at = models.DateField(default=timezone.localdate)
    due_date = models.DateField(blank=True, null=True)
    notes = models.TextField(blank=True)

    class Meta:
        indexes = [
            models.Index(fields=["customer", "status"]),
            models.Index(fields=["opened_at"]),
            models.Index(fields=["due_date"]),
        ]
        ordering = ["-opened_at", "customer__name"]
        verbose_name = "case"
        verbose_name_plural = "cases"

    def __str__(self) -> str:
        """Return case display label."""
        case_type = self.case_type.name if self.case_type else "Case"
        return f"{case_type} - {self.customer.name}"
