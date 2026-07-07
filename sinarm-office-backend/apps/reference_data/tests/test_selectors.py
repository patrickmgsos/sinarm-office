"""Tests for firearm reference data selectors."""

from __future__ import annotations

import pytest

from apps.common.models import ArchivableModel
from apps.reference_data.models import FirearmModel
from apps.reference_data.selectors import (
    calibers_active,
    firearm_models_active,
    firearm_models_for_caliber,
    firearm_models_for_manufacturer,
    manufacturers_active,
)
from apps.reference_data.services import (
    create_caliber,
    create_firearm_model,
    create_manufacturer,
)

pytestmark = pytest.mark.django_db


def test_active_selectors_exclude_archived_records() -> None:
    """Active selectors should exclude archived reference data."""
    manufacturer = create_manufacturer(name="Active Manufacturer")
    archived_manufacturer = create_manufacturer(name="Archived Manufacturer")
    caliber = create_caliber(name="Active Caliber")
    archived_caliber = create_caliber(name="Archived Caliber")
    firearm_model = create_firearm_model(
        manufacturer=manufacturer,
        name="Active Model",
        caliber=caliber,
    )
    archived_model = create_firearm_model(
        manufacturer=manufacturer,
        name="Archived Model",
        caliber=caliber,
    )
    archived_manufacturer.status = ArchivableModel.ArchiveStatus.ARCHIVED
    archived_manufacturer.save(update_fields=["status"])
    archived_caliber.status = ArchivableModel.ArchiveStatus.ARCHIVED
    archived_caliber.save(update_fields=["status"])
    archived_model.status = ArchivableModel.ArchiveStatus.ARCHIVED
    archived_model.save(update_fields=["status"])

    assert list(manufacturers_active()) == [manufacturer]
    assert list(calibers_active()) == [caliber]
    assert list(firearm_models_active()) == [firearm_model]


def test_firearm_model_scope_selectors() -> None:
    """Firearm model selectors should filter manufacturer and caliber scopes."""
    manufacturer = create_manufacturer(name="Taurus")
    other_manufacturer = create_manufacturer(name="Imbel")
    caliber = create_caliber(name="9mm")
    other_caliber = create_caliber(name=".380 ACP")
    expected = create_firearm_model(
        manufacturer=manufacturer,
        name="G3C",
        caliber=caliber,
    )
    create_firearm_model(
        manufacturer=other_manufacturer,
        name="MD1",
        caliber=caliber,
    )
    create_firearm_model(
        manufacturer=manufacturer,
        name="G2C",
        caliber=other_caliber,
    )

    assert list(
        firearm_models_for_manufacturer(manufacturer_id=manufacturer.id),
    ) == [
        FirearmModel.objects.get(manufacturer=manufacturer, name="G2C"),
        expected,
    ]
    assert list(firearm_models_for_caliber(caliber_id=caliber.id)) == [
        FirearmModel.objects.get(manufacturer=other_manufacturer, name="MD1"),
        expected,
    ]
