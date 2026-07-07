"""Customer address use cases."""

from __future__ import annotations

import uuid
from dataclasses import dataclass

from django.db import transaction

from apps.common.exceptions import BusinessRuleViolation, NotFoundException
from apps.customers.models import CustomerAddress
from apps.customers.repositories import CustomerRepository
from apps.reference_data.models import City, Country, State


@dataclass(frozen=True, slots=True)
class AddCustomerAddressData:
    """Input data for adding a customer address."""

    customer_id: uuid.UUID
    address_type: str
    street: str
    number: str = ""
    complement: str = ""
    district: str = ""
    postal_code: str = ""
    country: Country | None = None
    state: State | None = None
    city: City | None = None
    notes: str = ""
    is_primary: bool = False


class AddCustomerAddressService:
    """Use case for adding an address through the customer aggregate."""

    def __init__(self, *, repository: CustomerRepository | None = None) -> None:
        self.repository = repository or CustomerRepository()

    @transaction.atomic
    def execute(self, *, data: AddCustomerAddressData) -> CustomerAddress:
        """Add an address to a customer aggregate."""
        customer = self.repository.get_by_id(customer_id=data.customer_id)
        if customer is None:
            msg = "Customer was not found."
            raise NotFoundException(msg)

        street = data.street.strip()
        if not street:
            msg = "Customer address street is required."
            raise BusinessRuleViolation(msg)
        if data.address_type not in CustomerAddress.AddressType.values:
            msg = "Customer address type is invalid."
            raise BusinessRuleViolation(msg)

        if data.is_primary:
            self.repository.clear_primary_addresses(customer=customer)

        return self.repository.create_address(
            customer=customer,
            address_type=data.address_type,
            street=street,
            number=data.number.strip(),
            complement=data.complement.strip(),
            district=data.district.strip(),
            postal_code=data.postal_code.strip(),
            country=data.country,
            state=data.state,
            city=data.city,
            notes=data.notes,
            is_primary=data.is_primary,
        )
