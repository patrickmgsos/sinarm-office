"""Tests for firearm reference data models."""

from __future__ import annotations

import uuid

import pytest
from django.db import IntegrityError, transaction

from apps.common.models import ArchivableModel
from apps.reference_data.models import Caliber, FirearmModel, Manufacturer

pytestmark = pytest.mark.django_db


def test_manufacturer_uses_uuid_and_archive_status() -> None:
    """Manufacturer should use UUID identity and archive semantics."""
    manufacturer = Manufacturer.objects.create(name="Imbel", country="Brazil")

    assert isinstance(manufacturer.id, uuid.UUID)
    assert manufacturer.status == ArchivableModel.ArchiveStatus.ACTIVE


def test_caliber_uses_uuid_and_archive_status() -> None:
    """Caliber should use UUID identity and archive semantics."""
    caliber = Caliber.objects.create(name=".380 ACP", category="Pistol")

    assert isinstance(caliber.id, uuid.UUID)
    assert caliber.status == ArchivableModel.ArchiveStatus.ACTIVE


def test_firearm_model_links_manufacturer_and_optional_caliber() -> None:
    """FirearmModel should link manufacturer and optional caliber."""
    manufacturer = Manufacturer.objects.create(name="Taurus")
    caliber = Caliber.objects.create(name="9mm")
    firearm_model = FirearmModel.objects.create(
        manufacturer=manufacturer,
        name="G3C",
        caliber=caliber,
        species="Pistol",
        operation="Semi-automatic",
    )

    assert firearm_model.manufacturer == manufacturer
    assert firearm_model.caliber == caliber


def test_reference_data_uniqueness_constraints() -> None:
    """Reference data should enforce requested uniqueness constraints."""
    manufacturer = Manufacturer.objects.create(name="CBC")
    Manufacturer.objects.create(name="Other")
    Caliber.objects.create(name="12 GA")
    FirearmModel.objects.create(manufacturer=manufacturer, name="Model A")

    with pytest.raises(IntegrityError):
        with transaction.atomic():
            Manufacturer.objects.create(name="CBC")

    with pytest.raises(IntegrityError):
        with transaction.atomic():
            Caliber.objects.create(name="12 GA")

    with pytest.raises(IntegrityError):
        with transaction.atomic():
            FirearmModel.objects.create(manufacturer=manufacturer, name="Model A")
