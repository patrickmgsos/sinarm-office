"""Read selectors for the Customer Domain."""

from __future__ import annotations

from django.db.models import QuerySet

from apps.common.models import ArchivableModel
from apps.customers.models import Customer, CustomerAddress, CustomerContact


def customers_active() -> QuerySet[Customer]:
    """Return active customers ordered by name."""
    return Customer.objects.filter(
        status=ArchivableModel.ArchiveStatus.ACTIVE,
    ).order_by("name")


def customer_by_cpf(*, cpf: str) -> Customer | None:
    """Return an individual customer by normalized CPF."""
    return Customer.objects.filter(
        document_type=Customer.DocumentType.CPF,
        document_number=cpf,
    ).first()


def customer_addresses(*, customer: Customer) -> QuerySet[CustomerAddress]:
    """Return active addresses for a customer."""
    return CustomerAddress.objects.filter(
        customer=customer,
        status=ArchivableModel.ArchiveStatus.ACTIVE,
    ).order_by("-is_primary", "address_type", "street")


def customer_contacts(*, customer: Customer) -> QuerySet[CustomerContact]:
    """Return active contacts for a customer."""
    return CustomerContact.objects.filter(
        customer=customer,
        status=ArchivableModel.ArchiveStatus.ACTIVE,
    ).order_by("-is_primary", "contact_type", "value")
