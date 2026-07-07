"""Tests for customer lookup use cases."""

from __future__ import annotations

import pytest

from apps.common.exceptions import ValidationException
from apps.customers.models import Customer
from apps.customers.selectors import customer_by_cpf
from apps.customers.services import FindCustomerByCpfService, RegisterNewCustomerService

pytestmark = pytest.mark.django_db


def test_find_customer_by_cpf_returns_registered_customer() -> None:
    """Find Customer By CPF should return a matching individual customer."""
    registered = RegisterNewCustomerService().execute(
        name="Ada Lovelace",
        kind=Customer.CustomerKind.INDIVIDUAL,
        document_type=Customer.DocumentType.CPF,
        document_number="123.456.789-01",
    )

    found = FindCustomerByCpfService().execute(cpf="12345678901")

    assert found == registered.customer


def test_find_customer_by_cpf_returns_none_when_missing() -> None:
    """Find Customer By CPF should return None when no customer exists."""
    assert FindCustomerByCpfService().execute(cpf="00000000000") is None


def test_find_customer_by_cpf_rejects_invalid_cpf_shape() -> None:
    """Find Customer By CPF should validate CPF shape."""
    with pytest.raises(ValidationException):
        FindCustomerByCpfService().execute(cpf="123")


def test_customer_by_cpf_selector_returns_registered_customer() -> None:
    """Customer by CPF selector should return a registered customer."""
    registered = RegisterNewCustomerService().execute(
        name="Ada Lovelace",
        kind=Customer.CustomerKind.INDIVIDUAL,
        document_type=Customer.DocumentType.CPF,
        document_number="12345678901",
    )

    assert customer_by_cpf(cpf="12345678901") == registered.customer
