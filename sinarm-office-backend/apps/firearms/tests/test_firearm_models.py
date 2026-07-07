"""Tests for Firearm MVP models."""

from __future__ import annotations

import pytest
from django.db import IntegrityError

from apps.customers.models import Customer
from apps.customers.services import RegisterNewCustomerService
from apps.firearms.models import Firearm
from apps.reference_data.models import Caliber, FirearmModel, Manufacturer

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


def test_create_basic_firearm_record() -> None:
    """Firearm MVP should store a customer firearm record."""
    customer = _register_customer()
    manufacturer = Manufacturer.objects.create(name="Taurus")
    caliber = Caliber.objects.create(name="9mm")
    firearm_model = FirearmModel.objects.create(
        manufacturer=manufacturer,
        name="G2C",
        caliber=caliber,
    )

    firearm = Firearm.objects.create(
        customer=customer,
        manufacturer=manufacturer,
        model=firearm_model,
        caliber=caliber,
        serial_number="ABC123",
        sinarm_registration="SINARM-001",
    )

    assert firearm.customer == customer
    assert firearm.serial_number == "ABC123"
    assert str(firearm) == "Ada Lovelace - ABC123"


def test_firearm_serial_number_is_unique() -> None:
    """Firearm MVP should prevent duplicate serial numbers."""
    customer = _register_customer()
    Firearm.objects.create(customer=customer, serial_number="ABC123")

    with pytest.raises(IntegrityError):
        Firearm.objects.create(customer=customer, serial_number="ABC123")
