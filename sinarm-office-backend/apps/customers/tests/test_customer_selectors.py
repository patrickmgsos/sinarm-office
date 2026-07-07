"""Tests for Customer Domain selectors."""

from __future__ import annotations

import pytest

from apps.common.models import ArchivableModel
from apps.customers.models import Customer
from apps.customers.selectors import customers_active
from apps.customers.services import RegisterNewCustomerService

pytestmark = pytest.mark.django_db


def test_customers_active_excludes_archived_records() -> None:
    """Selector should return only active customers."""
    service = RegisterNewCustomerService()
    active = service.execute(
        name="Ada Lovelace",
        kind=Customer.CustomerKind.INDIVIDUAL,
        document_type=Customer.DocumentType.CPF,
        document_number="12345678901",
    ).customer
    archived = service.execute(
        name="Grace Hopper",
        kind=Customer.CustomerKind.INDIVIDUAL,
        document_type=Customer.DocumentType.CPF,
        document_number="98765432100",
    ).customer
    archived.status = ArchivableModel.ArchiveStatus.ARCHIVED
    archived.save(update_fields=["status"])

    assert list(customers_active()) == [active]
