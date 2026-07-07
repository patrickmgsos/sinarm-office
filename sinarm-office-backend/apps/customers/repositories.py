"""Persistence boundaries for the Customer Domain."""

from __future__ import annotations

import uuid

from apps.customers.models import Customer, CustomerAddress, CustomerContact
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
        rg_ie: str = "",
        phone: str = "",
        email: str = "",
        address: str = "",
        notes: str = "",
    ) -> Customer:
        """Persist a new customer aggregate root."""
        return Customer.objects.create(
            name=name,
            kind=kind,
            document_type=document_type,
            document_number=document_number,
            rg_ie=rg_ie,
            phone=phone,
            email=email,
            address=address,
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

    def contact_exists(
        self,
        *,
        customer: Customer,
        contact_type: str,
        value: str,
    ) -> bool:
        """Return whether a customer already has the contact value."""
        return CustomerContact.objects.filter(
            customer=customer,
            contact_type=contact_type,
            value=value,
        ).exists()

    def create_contact(
        self,
        *,
        customer: Customer,
        contact_type: str,
        value: str,
        label: str = "",
        notes: str = "",
        is_primary: bool = False,
    ) -> CustomerContact:
        """Persist a customer contact within the aggregate."""
        return CustomerContact.objects.create(
            customer=customer,
            contact_type=contact_type,
            value=value,
            label=label,
            notes=notes,
            is_primary=is_primary,
        )

    def clear_primary_contacts(
        self,
        *,
        customer: Customer,
        contact_type: str,
    ) -> None:
        """Mark existing customer contacts for a type as non-primary."""
        CustomerContact.objects.filter(
            customer=customer,
            contact_type=contact_type,
            is_primary=True,
        ).update(is_primary=False)
