"""Tests for firearm reference data services."""

from __future__ import annotations

import pytest

from apps.common.models import ArchivableModel
from apps.reference_data.services import (
    archive_caliber,
    archive_firearm_model,
    archive_manufacturer,
    create_caliber,
    create_firearm_model,
    create_manufacturer,
)

pytestmark = pytest.mark.django_db


def test_create_reference_data_services() -> None:
    """Services should create firearm reference records."""
    manufacturer = create_manufacturer(
        name="Taurus",
        country="Brazil",
        notes="Reference manufacturer",
    )
    caliber = create_caliber(
        name="9mm",
        category="Pistol",
        description="Reference caliber",
    )
    firearm_model = create_firearm_model(
        manufacturer=manufacturer,
        name="G3C",
        caliber=caliber,
        species="Pistol",
        operation="Semi-automatic",
        notes="Reference model",
    )

    assert manufacturer.name == "Taurus"
    assert caliber.name == "9mm"
    assert firearm_model.manufacturer == manufacturer
    assert firearm_model.caliber == caliber


def test_archive_reference_data_services() -> None:
    """Archive services should preserve reference data history."""
    manufacturer = create_manufacturer(name="Imbel")
    caliber = create_caliber(name=".380 ACP")
    firearm_model = create_firearm_model(
        manufacturer=manufacturer,
        name="MD1",
        caliber=caliber,
    )

    archive_manufacturer(manufacturer)
    archive_caliber(caliber)
    archive_firearm_model(firearm_model)

    assert manufacturer.status == ArchivableModel.ArchiveStatus.ARCHIVED
    assert caliber.status == ArchivableModel.ArchiveStatus.ARCHIVED
    assert firearm_model.status == ArchivableModel.ArchiveStatus.ARCHIVED
