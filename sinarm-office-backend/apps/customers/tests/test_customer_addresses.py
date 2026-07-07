"""Tests for customer address use cases."""

from __future__ import annotations

import uuid

import pytest

from apps.common.exceptions import BusinessRuleViolation, NotFoundException
from apps.customers.models import Customer, CustomerAddress
from apps.customers.selectors import customer_addresses
from apps.customers.services import (
    AddCustomerAddressData,
    AddCustomerAddressService,
    RegisterNewCustomerService,
)
from apps.reference_data.models import City, Country, State

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


def test_add_customer_address_creates_address_for_customer() -> None:
    """Add Customer Address should create an address owned by the aggregate."""
    customer = _register_customer()

    address = AddCustomerAddressService().execute(
        data=AddCustomerAddressData(
            customer_id=customer.id,
            address_type=CustomerAddress.AddressType.RESIDENTIAL,
            street=" Rua das Flores ",
            number="123",
            is_primary=True,
        ),
    )

    assert address.customer == customer
    assert address.street == "Rua das Flores"
    assert address.is_primary is True


def test_add_customer_address_can_reference_geographic_data() -> None:
    """Add Customer Address should support optional geographic references."""
    customer = _register_customer()
    country = Country.objects.create(name="Brasil", iso2="BR", iso3="BRA")
    state = State.objects.create(country=country, name="Sao Paulo", code="SP")
    city = City.objects.create(state=state, name="Sao Paulo", ibge_code="3550308")

    address = AddCustomerAddressService().execute(
        data=AddCustomerAddressData(
            customer_id=customer.id,
            address_type=CustomerAddress.AddressType.COMMERCIAL,
            street="Avenida Paulista",
            country=country,
            state=state,
            city=city,
        ),
    )

    assert address.country == country
    assert address.state == state
    assert address.city == city


def test_add_primary_customer_address_demotes_existing_primary_address() -> None:
    """Add Customer Address should keep one primary address per customer."""
    customer = _register_customer()
    service = AddCustomerAddressService()
    first = service.execute(
        data=AddCustomerAddressData(
            customer_id=customer.id,
            address_type=CustomerAddress.AddressType.RESIDENTIAL,
            street="First Street",
            is_primary=True,
        ),
    )

    second = service.execute(
        data=AddCustomerAddressData(
            customer_id=customer.id,
            address_type=CustomerAddress.AddressType.COMMERCIAL,
            street="Second Street",
            is_primary=True,
        ),
    )

    first.refresh_from_db()
    assert first.is_primary is False
    assert second.is_primary is True


def test_add_customer_address_rejects_unknown_customer() -> None:
    """Add Customer Address should reject unknown customers."""
    with pytest.raises(NotFoundException):
        AddCustomerAddressService().execute(
            data=AddCustomerAddressData(
                customer_id=uuid.uuid4(),
                address_type=CustomerAddress.AddressType.RESIDENTIAL,
                street="Rua das Flores",
            ),
        )


def test_add_customer_address_rejects_missing_street() -> None:
    """Add Customer Address should require street."""
    customer = _register_customer()

    with pytest.raises(BusinessRuleViolation):
        AddCustomerAddressService().execute(
            data=AddCustomerAddressData(
                customer_id=customer.id,
                address_type=CustomerAddress.AddressType.RESIDENTIAL,
                street=" ",
            ),
        )


def test_customer_addresses_selector_returns_active_addresses() -> None:
    """Customer addresses selector should return active addresses."""
    customer = _register_customer()
    address = AddCustomerAddressService().execute(
        data=AddCustomerAddressData(
            customer_id=customer.id,
            address_type=CustomerAddress.AddressType.RESIDENTIAL,
            street="Rua das Flores",
        ),
    )

    assert list(customer_addresses(customer=customer)) == [address]
