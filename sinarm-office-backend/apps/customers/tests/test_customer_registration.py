"""Tests for Register New Customer use case."""

from __future__ import annotations

import uuid

import pytest

from apps.common.exceptions import BusinessRuleViolation
from apps.common.models import ArchivableModel
from apps.customers.events import CustomerRegistered
from apps.customers.models import Customer
from apps.customers.services import RegisterNewCustomerService

pytestmark = pytest.mark.django_db


def test_register_new_individual_customer() -> None:
    """Register New Customer should create an individual customer aggregate."""
    result = RegisterNewCustomerService().execute(
        name=" Ada Lovelace ",
        kind=Customer.CustomerKind.INDIVIDUAL,
        document_type=Customer.DocumentType.CPF,
        document_number="123.456.789-01",
        notes="First customer",
    )

    assert isinstance(result.customer.id, uuid.UUID)
    assert result.customer.name == "Ada Lovelace"
    assert result.customer.document_number == "12345678901"
    assert result.customer.status == ArchivableModel.ArchiveStatus.ACTIVE
    assert isinstance(result.event, CustomerRegistered)
    assert result.event.customer_id == result.customer.id


def test_register_new_company_customer() -> None:
    """Register New Customer should support CNPJ for company customers."""
    result = RegisterNewCustomerService().execute(
        name="SINARM Office LTDA",
        kind=Customer.CustomerKind.COMPANY,
        document_type=Customer.DocumentType.CNPJ,
        document_number="12.345.678/0001-90",
    )

    assert result.customer.document_number == "12345678000190"
    assert result.customer.kind == Customer.CustomerKind.COMPANY


def test_register_new_customer_rejects_duplicate_document() -> None:
    """Register New Customer should reject duplicate CPF/CNPJ values."""
    service = RegisterNewCustomerService()
    service.execute(
        name="Ada Lovelace",
        kind=Customer.CustomerKind.INDIVIDUAL,
        document_type=Customer.DocumentType.CPF,
        document_number="12345678901",
    )

    with pytest.raises(BusinessRuleViolation):
        service.execute(
            name="Ada Byron",
            kind=Customer.CustomerKind.INDIVIDUAL,
            document_type=Customer.DocumentType.CPF,
            document_number="123.456.789-01",
        )


def test_register_new_customer_rejects_invalid_document_shape() -> None:
    """Register New Customer should enforce basic CPF/CNPJ shape."""
    with pytest.raises(BusinessRuleViolation):
        RegisterNewCustomerService().execute(
            name="Invalid Customer",
            kind=Customer.CustomerKind.INDIVIDUAL,
            document_type=Customer.DocumentType.CPF,
            document_number="123",
        )


def test_register_new_customer_rejects_kind_document_mismatch() -> None:
    """Register New Customer should align customer kind and document type."""
    with pytest.raises(BusinessRuleViolation):
        RegisterNewCustomerService().execute(
            name="Mismatch Customer",
            kind=Customer.CustomerKind.COMPANY,
            document_type=Customer.DocumentType.CPF,
            document_number="12345678901",
        )
