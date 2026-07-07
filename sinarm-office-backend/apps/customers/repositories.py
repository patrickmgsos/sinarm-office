"""Persistence boundaries for the Customer Domain."""

from __future__ import annotations

import uuid

from apps.customers.models import Customer, CustomerAddress
from apps.reference_data.models import City, Country, State


class CustomerRepository:
    """Repository for customer aggregate persistence."""

    def create(
        self,
        *,
        name: str,
        kind: str,
        document_type: str,
        document_number: str,
        notes: str = "",
    ) -> Customer:
        """Persist a new customer aggregate root."""
        return Customer.objects.create(
            name=name,
            kind=kind,
            document_type=document_type,
            document_number=document_number,
            notes=notes,
        )

    def exists_by_document_number(self, *, document_number: str) -> bool:
        """Return whether a customer exists with the document number."""
        return Customer.objects.filter(document_number=document_number).exists()

    def find_by_cpf(self, *, cpf: str) -> Customer | None:
        """Return an individual customer by CPF, when registered."""
        return Customer.objects.filter(
            document_type=Customer.DocumentType.CPF,
            document_number=cpf,
        ).first()

    def get_by_id(self, *, customer_id: uuid.UUID) -> Customer | None:
        """Return a customer aggregate by UUID."""
        return Customer.objects.filter(id=customer_id).first()

    def save(self, *, customer: Customer, update_fields: list[str]) -> Customer:
        """Persist changes to an existing customer aggregate."""
        customer.save(update_fields=update_fields)
        return customer

    def create_address(
        self,
        *,
        customer: Customer,
        address_type: str,
        street: str,
        number: str = "",
        complement: str = "",
        district: str = "",
        postal_code: str = "",
        country: Country | None = None,
        state: State | None = None,
        city: City | None = None,
        notes: str = "",
        is_primary: bool = False,
    ) -> CustomerAddress:
        """Persist a customer address within the aggregate."""
        return CustomerAddress.objects.create(
            customer=customer,
            address_type=address_type,
            street=street,
            number=number,
            complement=complement,
            district=district,
            postal_code=postal_code,
            country=country,
            state=state,
            city=city,
            notes=notes,
            is_primary=is_primary,
        )

    def clear_primary_addresses(self, *, customer: Customer) -> None:
        """Mark existing customer addresses as non-primary."""
        CustomerAddress.objects.filter(
            customer=customer,
            is_primary=True,
        ).update(is_primary=False)
