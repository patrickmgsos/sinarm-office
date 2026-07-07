"""Customer contact use cases."""

from __future__ import annotations

import uuid
from dataclasses import dataclass

from django.db import transaction

from apps.common.exceptions import BusinessRuleViolation, NotFoundException
from apps.customers.models import CustomerContact
from apps.customers.repositories import CustomerRepository


@dataclass(frozen=True, slots=True)
class AddCustomerContactData:
    """Input data for adding a customer contact."""

    customer_id: uuid.UUID
    contact_type: str
    value: str
    label: str = ""
    notes: str = ""
    is_primary: bool = False


def normalize_contact_value(*, contact_type: str, value: str) -> str:
    """Normalize a customer contact value for storage."""
    normalized_value = value.strip()
    if contact_type == CustomerContact.ContactType.EMAIL:
        return normalized_value.lower()
    if contact_type in (
        CustomerContact.ContactType.PHONE,
        CustomerContact.ContactType.WHATSAPP,
    ):
        return "".join(
            character for character in normalized_value if character.isdigit()
        )
    return normalized_value


class AddCustomerContactService:
    """Use case for adding a contact through the customer aggregate."""

    def __init__(self, *, repository: CustomerRepository | None = None) -> None:
        self.repository = repository or CustomerRepository()

    @transaction.atomic
    def execute(self, *, data: AddCustomerContactData) -> CustomerContact:
        """Add a contact to a customer aggregate."""
        customer = self.repository.get_by_id(customer_id=data.customer_id)
        if customer is None:
            msg = "Customer was not found."
            raise NotFoundException(msg)

        if data.contact_type not in CustomerContact.ContactType.values:
            msg = "Customer contact type is invalid."
            raise BusinessRuleViolation(msg)

        value = normalize_contact_value(
            contact_type=data.contact_type,
            value=data.value,
        )
        self._enforce_value(contact_type=data.contact_type, value=value)

        if self.repository.contact_exists(
            customer=customer,
            contact_type=data.contact_type,
            value=value,
        ):
            msg = "Customer contact already exists."
            raise BusinessRuleViolation(msg)

        if data.is_primary:
            self.repository.clear_primary_contacts(
                customer=customer,
                contact_type=data.contact_type,
            )

        return self.repository.create_contact(
            customer=customer,
            contact_type=data.contact_type,
            value=value,
            label=data.label.strip(),
            notes=data.notes,
            is_primary=data.is_primary,
        )

    def _enforce_value(self, *, contact_type: str, value: str) -> None:
        """Enforce basic contact value validation."""
        if contact_type == CustomerContact.ContactType.EMAIL:
            if "@" not in value or "." not in value.rsplit("@", maxsplit=1)[-1]:
                msg = "Customer email contact is invalid."
                raise BusinessRuleViolation(msg)
            return

        if contact_type in (
            CustomerContact.ContactType.PHONE,
            CustomerContact.ContactType.WHATSAPP,
        ):
            if not value.isdigit() or not 8 <= len(value) <= 15:
                msg = "Customer phone contact must contain 8 to 15 digits."
                raise BusinessRuleViolation(msg)
            return

        msg = "Customer contact value is invalid."
        raise BusinessRuleViolation(msg)
