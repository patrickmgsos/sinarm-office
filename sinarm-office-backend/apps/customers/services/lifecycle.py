"""Customer lifecycle use cases."""

from __future__ import annotations

import uuid
from typing import TYPE_CHECKING

from django.db import transaction
from django.utils import timezone

from apps.common.exceptions import NotFoundException
from apps.common.models import ArchivableModel
from apps.customers.models import Customer
from apps.customers.repositories import CustomerRepository

if TYPE_CHECKING:
    from apps.identity.models import CustomUser


class ArchiveCustomerService:
    """Use case for archiving a customer aggregate."""

    def __init__(self, *, repository: CustomerRepository | None = None) -> None:
        self.repository = repository or CustomerRepository()

    @transaction.atomic
    def execute(
        self,
        *,
        customer_id: uuid.UUID,
        archived_by: CustomUser | None = None,
    ) -> Customer:
        """Archive a customer without deleting it."""
        customer = self.repository.get_by_id(customer_id=customer_id)
        if customer is None:
            msg = "Customer was not found."
            raise NotFoundException(msg)

        customer.status = ArchivableModel.ArchiveStatus.ARCHIVED
        customer.archived_at = timezone.now()
        customer.archived_by = archived_by
        return self.repository.save(
            customer=customer,
            update_fields=["status", "archived_at", "archived_by", "updated_at"],
        )


class RestoreCustomerService:
    """Use case for restoring an archived customer aggregate."""

    def __init__(self, *, repository: CustomerRepository | None = None) -> None:
        self.repository = repository or CustomerRepository()

    @transaction.atomic
    def execute(self, *, customer_id: uuid.UUID) -> Customer:
        """Restore an archived customer to active status."""
        customer = self.repository.get_by_id(customer_id=customer_id)
        if customer is None:
            msg = "Customer was not found."
            raise NotFoundException(msg)

        customer.status = ArchivableModel.ArchiveStatus.ACTIVE
        customer.archived_at = None
        customer.archived_by = None
        return self.repository.save(
            customer=customer,
            update_fields=["status", "archived_at", "archived_by", "updated_at"],
        )
