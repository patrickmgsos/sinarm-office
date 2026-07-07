"""Tests for customer lifecycle use cases."""

from __future__ import annotations

import uuid

import pytest

from apps.common.exceptions import NotFoundException
from apps.common.models import ArchivableModel
from apps.customers.models import Customer
from apps.customers.services import (
    ArchiveCustomerService,
    RegisterNewCustomerService,
    RestoreCustomerService,
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


def test_archive_customer_marks_customer_as_archived() -> None:
    """Archive Customer should mark the aggregate as archived."""
    customer = _register_customer()

    archived = ArchiveCustomerService().execute(customer_id=customer.id)

    assert archived.status == ArchivableModel.ArchiveStatus.ARCHIVED
    assert archived.archived_at is not None


def test_restore_customer_marks_customer_as_active() -> None:
    """Restore Customer should reactivate an archived aggregate."""
    customer = _register_customer()
    ArchiveCustomerService().execute(customer_id=customer.id)

    restored = RestoreCustomerService().execute(customer_id=customer.id)

    assert restored.status == ArchivableModel.ArchiveStatus.ACTIVE
    assert restored.archived_at is None
    assert restored.archived_by is None


def test_archive_customer_rejects_unknown_customer() -> None:
    """Archive Customer should reject unknown customer IDs."""
    with pytest.raises(NotFoundException):
        ArchiveCustomerService().execute(customer_id=uuid.uuid4())


def test_restore_customer_rejects_unknown_customer() -> None:
    """Restore Customer should reject unknown customer IDs."""
    with pytest.raises(NotFoundException):
        RestoreCustomerService().execute(customer_id=uuid.uuid4())
