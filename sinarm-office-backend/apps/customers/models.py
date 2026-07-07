"""Customer aggregate root models."""

from __future__ import annotations

from django.db import models

from apps.common.models import ArchivableModel, BaseModel
from apps.reference_data.models import City, Country, State


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


class CustomerAddress(BaseModel, ArchivableModel):
    """Address owned by a customer aggregate."""

    class AddressType(models.TextChoices):
        RESIDENTIAL = "residential", "Residential"
        COMMERCIAL = "commercial", "Commercial"
        OTHER = "other", "Other"

    customer = models.ForeignKey(
        Customer,
        on_delete=models.CASCADE,
        related_name="addresses",
    )
    address_type = models.CharField(max_length=32, choices=AddressType.choices)
    street = models.CharField(max_length=180)
    number = models.CharField(max_length=32, blank=True)
    complement = models.CharField(max_length=120, blank=True)
    district = models.CharField(max_length=120, blank=True)
    postal_code = models.CharField(max_length=16, blank=True)
    country = models.ForeignKey(
        Country,
        blank=True,
        null=True,
        on_delete=models.PROTECT,
        related_name="customer_addresses",
    )
    state = models.ForeignKey(
        State,
        blank=True,
        null=True,
        on_delete=models.PROTECT,
        related_name="customer_addresses",
    )
    city = models.ForeignKey(
        City,
        blank=True,
        null=True,
        on_delete=models.PROTECT,
        related_name="customer_addresses",
    )
    notes = models.TextField(blank=True)
    is_primary = models.BooleanField(default=False)

    class Meta:
        indexes = [
            models.Index(fields=["customer", "address_type"]),
            models.Index(fields=["customer", "is_primary"]),
        ]
        ordering = ["customer__name", "-is_primary", "address_type", "street"]
        verbose_name = "customer address"
        verbose_name_plural = "customer addresses"

    def __str__(self) -> str:
        """Return address display label."""
        return f"{self.customer.name} - {self.street}"


class CustomerContact(BaseModel, ArchivableModel):
    """Contact channel owned by a customer aggregate."""

    class ContactType(models.TextChoices):
        PHONE = "phone", "Phone"
        EMAIL = "email", "Email"
        WHATSAPP = "whatsapp", "WhatsApp"

    customer = models.ForeignKey(
        Customer,
        on_delete=models.CASCADE,
        related_name="contacts",
    )
    contact_type = models.CharField(max_length=32, choices=ContactType.choices)
    value = models.CharField(max_length=180)
    label = models.CharField(max_length=80, blank=True)
    notes = models.TextField(blank=True)
    is_primary = models.BooleanField(default=False)

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=["customer", "contact_type", "value"],
                name="ux_customer_contact_customer_type_value",
            ),
        ]
        indexes = [
            models.Index(fields=["customer", "contact_type"]),
            models.Index(fields=["customer", "is_primary"]),
        ]
        ordering = ["customer__name", "-is_primary", "contact_type", "value"]
        verbose_name = "customer contact"
        verbose_name_plural = "customer contacts"

    def __str__(self) -> str:
        """Return contact display label."""
        return f"{self.customer.name} - {self.value}"
