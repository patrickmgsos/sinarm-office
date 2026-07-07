"""Tests for customer contact use cases."""

from __future__ import annotations

import uuid

import pytest

from apps.common.exceptions import BusinessRuleViolation, NotFoundException
from apps.customers.models import Customer, CustomerContact
from apps.customers.selectors import customer_contacts
from apps.customers.services import (
    AddCustomerContactData,
    AddCustomerContactService,
    RegisterNewCustomerService,
)

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


def test_add_customer_email_contact_creates_normalized_contact() -> None:
    """Add Customer Contact should create normalized email contacts."""
    customer = _register_customer()

    contact = AddCustomerContactService().execute(
        data=AddCustomerContactData(
            customer_id=customer.id,
            contact_type=CustomerContact.ContactType.EMAIL,
            value=" ADA@EXAMPLE.COM ",
            label="Work",
            is_primary=True,
        ),
    )

    assert contact.customer == customer
    assert contact.value == "ada@example.com"
    assert contact.label == "Work"
    assert contact.is_primary is True


def test_add_customer_phone_contact_creates_digits_only_contact() -> None:
    """Add Customer Contact should normalize phone contacts to digits."""
    customer = _register_customer()

    contact = AddCustomerContactService().execute(
        data=AddCustomerContactData(
            customer_id=customer.id,
            contact_type=CustomerContact.ContactType.PHONE,
            value="(11) 9999-8888",
        ),
    )

    assert contact.value == "1199998888"


def test_add_customer_whatsapp_contact_creates_digits_only_contact() -> None:
    """Add Customer Contact should support WhatsApp contacts."""
    customer = _register_customer()

    contact = AddCustomerContactService().execute(
        data=AddCustomerContactData(
            customer_id=customer.id,
            contact_type=CustomerContact.ContactType.WHATSAPP,
            value="+55 11 99999-8888",
        ),
    )

    assert contact.value == "5511999998888"


def test_add_primary_customer_contact_demotes_existing_primary_contact() -> None:
    """Add Customer Contact should keep one primary contact per type."""
    customer = _register_customer()
    service = AddCustomerContactService()
    first = service.execute(
        data=AddCustomerContactData(
            customer_id=customer.id,
            contact_type=CustomerContact.ContactType.EMAIL,
            value="first@example.com",
            is_primary=True,
        ),
    )

    second = service.execute(
        data=AddCustomerContactData(
            customer_id=customer.id,
            contact_type=CustomerContact.ContactType.EMAIL,
            value="second@example.com",
            is_primary=True,
        ),
    )

    first.refresh_from_db()
    assert first.is_primary is False
    assert second.is_primary is True


def test_add_customer_contact_rejects_duplicate_contact() -> None:
    """Add Customer Contact should reject duplicate contact values."""
    customer = _register_customer()
    service = AddCustomerContactService()
    service.execute(
        data=AddCustomerContactData(
            customer_id=customer.id,
            contact_type=CustomerContact.ContactType.EMAIL,
            value="ada@example.com",
        ),
    )

    with pytest.raises(BusinessRuleViolation):
        service.execute(
            data=AddCustomerContactData(
                customer_id=customer.id,
                contact_type=CustomerContact.ContactType.EMAIL,
                value=" ADA@EXAMPLE.COM ",
            ),
        )


def test_add_customer_contact_rejects_invalid_email() -> None:
    """Add Customer Contact should reject invalid emails."""
    customer = _register_customer()

    with pytest.raises(BusinessRuleViolation):
        AddCustomerContactService().execute(
            data=AddCustomerContactData(
                customer_id=customer.id,
                contact_type=CustomerContact.ContactType.EMAIL,
                value="not-an-email",
            ),
        )


def test_add_customer_contact_rejects_unknown_customer() -> None:
    """Add Customer Contact should reject unknown customers."""
    with pytest.raises(NotFoundException):
        AddCustomerContactService().execute(
            data=AddCustomerContactData(
                customer_id=uuid.uuid4(),
                contact_type=CustomerContact.ContactType.PHONE,
                value="1199998888",
            ),
        )


def test_customer_contacts_selector_returns_active_contacts() -> None:
    """Customer contacts selector should return active contacts."""
    customer = _register_customer()
    contact = AddCustomerContactService().execute(
        data=AddCustomerContactData(
            customer_id=customer.id,
            contact_type=CustomerContact.ContactType.EMAIL,
            value="ada@example.com",
        ),
    )

    assert list(customer_contacts(customer=customer)) == [contact]
