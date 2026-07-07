"""Register New Customer use case."""

from __future__ import annotations

from dataclasses import dataclass

from django.db import transaction
from django.utils import timezone

from apps.customers.events import CustomerRegistered
from apps.customers.models import Customer
from apps.customers.policies import CustomerRegistrationPolicy
from apps.customers.repositories import CustomerRepository
from apps.customers.specifications import CustomerCanBeRegisteredSpecification


def normalize_document_number(document_number: str) -> str:
    """Return only digits from a CPF/CNPJ value."""
    return "".join(character for character in document_number if character.isdigit())


@dataclass(frozen=True, slots=True)
class RegisterNewCustomerResult:
    """Result of registering a new customer."""

    customer: Customer
    event: CustomerRegistered


class RegisterNewCustomerService:
    """Use case for registering a new customer aggregate root."""

    def __init__(
        self,
        *,
        repository: CustomerRepository | None = None,
        policy: CustomerRegistrationPolicy | None = None,
    ) -> None:
        self.repository = repository or CustomerRepository()
        self.policy = policy or CustomerRegistrationPolicy(
            repository=self.repository,
            specification=CustomerCanBeRegisteredSpecification(),
        )

    @transaction.atomic
    def execute(
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
    ) -> RegisterNewCustomerResult:
        """Register a new customer."""
        normalized_document_number = normalize_document_number(document_number)
        normalized_name = name.strip()

        self.policy.enforce(
            name=normalized_name,
            kind=kind,
            document_type=document_type,
            document_number=normalized_document_number,
        )
        customer = self.repository.create(
            name=normalized_name,
            kind=kind,
            document_type=document_type,
            document_number=normalized_document_number,
            rg_ie=rg_ie.strip(),
            phone=phone.strip(),
            email=email.strip().lower(),
            address=address.strip(),
            notes=notes,
        )
        event = CustomerRegistered(
            customer_id=customer.id,
            name=customer.name,
            document_type=customer.document_type,
            document_number=customer.document_number,
            occurred_at=timezone.now(),
        )
        return RegisterNewCustomerResult(customer=customer, event=event)
