"""Customer aggregate root models."""

from __future__ import annotations

from django.db import models

from apps.common.models import ArchivableModel, BaseModel


class Customer(BaseModel, ArchivableModel):
    """Customer aggregate root."""

    class CustomerKind(models.TextChoices):
        INDIVIDUAL = "individual", "Individual"
        COMPANY = "company", "Company"

    class DocumentType(models.TextChoices):
        CPF = "cpf", "CPF"
        CNPJ = "cnpj", "CNPJ"

    name = models.CharField(max_length=180)
    kind = models.CharField(max_length=32, choices=CustomerKind.choices)
    document_type = models.CharField(max_length=16, choices=DocumentType.choices)
    document_number = models.CharField(max_length=14, unique=True, db_index=True)
    notes = models.TextField(blank=True)

    class Meta:
        indexes = [
            models.Index(fields=["document_type", "document_number"]),
            models.Index(fields=["status", "name"]),
        ]
        ordering = ["name"]
        verbose_name = "customer"
        verbose_name_plural = "customers"

    def __str__(self) -> str:
        """Return customer display name."""
        return self.name
