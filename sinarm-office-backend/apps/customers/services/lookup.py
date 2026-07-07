"""Customer lookup use cases."""

from __future__ import annotations

from apps.common.exceptions import ValidationException
from apps.customers.models import Customer
from apps.customers.repositories import CustomerRepository
from apps.customers.services.registration import normalize_document_number


class FindCustomerByCpfService:
    """Use case for finding a customer by CPF."""

    def __init__(self, *, repository: CustomerRepository | None = None) -> None:
        self.repository = repository or CustomerRepository()

    def execute(self, *, cpf: str) -> Customer | None:
        """Find an individual customer by CPF."""
        normalized_cpf = normalize_document_number(cpf)
        if len(normalized_cpf) != 11:
            msg = "CPF must contain 11 digits."
            raise ValidationException(msg)

        return self.repository.find_by_cpf(cpf=normalized_cpf)
