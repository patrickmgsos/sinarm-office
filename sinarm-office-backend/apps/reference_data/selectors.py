"""Query helpers for firearm reference data."""

from __future__ import annotations

import uuid

from django.db.models import QuerySet

from apps.common.models import ArchivableModel
from apps.reference_data.models import Caliber, FirearmModel, Manufacturer


def manufacturers_active() -> QuerySet[Manufacturer]:
    """Return active manufacturers ordered by name."""
    return Manufacturer.objects.filter(
        status=ArchivableModel.ArchiveStatus.ACTIVE,
    ).order_by("name")


def calibers_active() -> QuerySet[Caliber]:
    """Return active calibers ordered by name."""
    return Caliber.objects.filter(
        status=ArchivableModel.ArchiveStatus.ACTIVE,
    ).order_by("name")


def firearm_models_active() -> QuerySet[FirearmModel]:
    """Return active firearm models with reference relationships loaded."""
    return (
        FirearmModel.objects.filter(status=ArchivableModel.ArchiveStatus.ACTIVE)
        .select_related("manufacturer", "caliber")
        .order_by("manufacturer__name", "name")
    )


def firearm_models_for_manufacturer(
    *,
    manufacturer_id: uuid.UUID,
    active_only: bool = True,
) -> QuerySet[FirearmModel]:
    """Return firearm models for a manufacturer."""
    queryset = FirearmModel.objects.filter(
        manufacturer_id=manufacturer_id,
    ).select_related("manufacturer", "caliber")
    if active_only:
        queryset = queryset.filter(status=ArchivableModel.ArchiveStatus.ACTIVE)

    return queryset.order_by("name")


def firearm_models_for_caliber(
    *,
    caliber_id: uuid.UUID,
    active_only: bool = True,
) -> QuerySet[FirearmModel]:
    """Return firearm models for a caliber."""
    queryset = FirearmModel.objects.filter(caliber_id=caliber_id).select_related(
        "manufacturer",
        "caliber",
    )
    if active_only:
        queryset = queryset.filter(status=ArchivableModel.ArchiveStatus.ACTIVE)

    return queryset.order_by("manufacturer__name", "name")
