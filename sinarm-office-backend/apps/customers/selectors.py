"""Read selectors for the Customer Domain."""

from __future__ import annotations

from django.db.models import QuerySet

from apps.common.models import ArchivableModel
from apps.customers.models import Customer


def customers_active() -> QuerySet[Customer]:
    """Return active customers ordered by name."""
    return Customer.objects.filter(
        status=ArchivableModel.ArchiveStatus.ACTIVE,
    ).order_by("name")
