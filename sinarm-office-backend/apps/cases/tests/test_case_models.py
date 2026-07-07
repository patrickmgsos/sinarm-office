"""Tests for Case MVP models."""

from __future__ import annotations

import pytest
from django.utils import timezone

from apps.cases.models import Case
from apps.customers.models import Customer
from apps.customers.services import RegisterNewCustomerService
from apps.reference_data.models import CaseType, StatusType

pytestmark = pytest.mark.django_db


def _register_customer() -> Customer:
    return (
        RegisterNewCustomerService()
        .execute(
            name="Ada Lovelace",
            kind=Customer.CustomerKind.INDIVIDUAL,
            document_type=Customer.DocumentType.CPF,
            document_number="12345678901",
        )
        .customer
    )


def test_create_basic_case_record() -> None:
    """Case MVP should store an operational case record."""
    customer = _register_customer()
    case_type = CaseType.objects.create(name="Renewal", code="renewal")
    status_type = StatusType.objects.create(name="Open", code="open")

    case = Case.objects.create(
        customer=customer,
        case_type=case_type,
        status_type=status_type,
        due_date=timezone.localdate(),
        notes="Client needs renewal.",
    )

    assert case.customer == customer
    assert case.case_type == case_type
    assert case.status_type == status_type
    assert str(case) == "Renewal - Ada Lovelace"
