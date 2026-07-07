"""Customer registration policies."""

from __future__ import annotations

from apps.common.exceptions import BusinessRuleViolation
from apps.customers.models import Customer
from apps.customers.repositories import CustomerRepository
from apps.customers.specifications import CustomerCanBeRegisteredSpecification


class CustomerRegistrationPolicy:
    """Policy for registering new customers."""

    def __init__(
        self,
        *,
        repository: CustomerRepository,
        specification: CustomerCanBeRegisteredSpecification,
    ) -> None:
        self.repository = repository
        self.specification = specification

    def enforce(
        self,
        *,
        name: str,
        kind: str,
        document_type: str,
        document_number: str,
    ) -> None:
        """Raise when a customer cannot be registered."""
        if not self.specification.is_satisfied_by(
            name=name,
            kind=kind,
            document_type=document_type,
            document_number=document_number,
        ):
            msg = "Customer registration data is invalid."
            raise BusinessRuleViolation(msg)

        if self.repository.exists_by_document_number(
            document_number=document_number,
        ):
            msg = "A customer with this CPF/CNPJ is already registered."
            raise BusinessRuleViolation(msg)

        if kind == Customer.CustomerKind.INDIVIDUAL:
            expected_document_type = Customer.DocumentType.CPF
        else:
            expected_document_type = Customer.DocumentType.CNPJ

        if document_type != expected_document_type:
            msg = "Customer kind and document type do not match."
            raise BusinessRuleViolation(msg)
