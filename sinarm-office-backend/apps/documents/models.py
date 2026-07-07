"""Document generation MVP models."""

from __future__ import annotations

from django.db import models
from django.utils import timezone

from apps.cases.models import Case
from apps.common.models import ArchivableModel, BaseModel
from apps.customers.models import Customer


class GeneratedDocument(BaseModel, ArchivableModel):
    """Generated DOCX document record for the MVP."""

    class TemplateType(models.TextChoices):
        RENEWAL_NEED = "renewal_need", "Efetiva necessidade de renovacao"
        CERTIFICATE_AUTHORIZATION = (
            "certificate_authorization",
            "Autorizacao para certidoes",
        )
        SIMPLE_POWER_OF_ATTORNEY = "simple_power_of_attorney", "Procuracao simples"

    customer = models.ForeignKey(
        Customer,
        on_delete=models.PROTECT,
        related_name="generated_documents",
    )
    case = models.ForeignKey(
        Case,
        blank=True,
        null=True,
        on_delete=models.SET_NULL,
        related_name="generated_documents",
    )
    template_type = models.CharField(max_length=64, choices=TemplateType.choices)
    title = models.CharField(max_length=180)
    file = models.FileField(upload_to="generated_documents/")
    generated_at = models.DateTimeField(default=timezone.now)
    notes = models.TextField(blank=True)

    class Meta:
        indexes = [
            models.Index(fields=["customer", "template_type"]),
            models.Index(fields=["generated_at"]),
        ]
        ordering = ["-generated_at", "customer__name"]
        verbose_name = "generated document"
        verbose_name_plural = "generated documents"

    def __str__(self) -> str:
        """Return generated document display label."""
        return f"{self.title} - {self.customer.name}"
