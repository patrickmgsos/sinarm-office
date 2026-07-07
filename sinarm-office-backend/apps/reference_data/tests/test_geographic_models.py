"""Tests for geographic reference data models."""

from __future__ import annotations

import uuid

import pytest
from django.db import IntegrityError, transaction

from apps.common.models import ArchivableModel
from apps.reference_data.models import City, Country, State

pytestmark = pytest.mark.django_db


def test_country_uses_uuid_and_archive_status() -> None:
    """Country should use UUID identity and archive semantics."""
    country = Country.objects.create(name="Brazil", iso2="BR", iso3="BRA")

    assert isinstance(country.id, uuid.UUID)
    assert country.status == ArchivableModel.ArchiveStatus.ACTIVE


def test_state_and_city_hierarchy() -> None:
    """State and City should preserve geographic hierarchy."""
    country = Country.objects.create(name="Brazil", iso2="BR", iso3="BRA")
    state = State.objects.create(country=country, name="Sao Paulo", code="SP")
    city = City.objects.create(state=state, name="Sao Paulo", ibge_code="3550308")

    assert state.country == country
    assert city.state == state


def test_geographic_uniqueness_constraints() -> None:
    """Geographic data should enforce requested uniqueness constraints."""
    country = Country.objects.create(name="Brazil", iso2="BR", iso3="BRA")
    state = State.objects.create(country=country, name="Sao Paulo", code="SP")
    City.objects.create(state=state, name="Sao Paulo")

    with pytest.raises(IntegrityError):
        with transaction.atomic():
            Country.objects.create(name="Brazil 2", iso2="BR", iso3="BR2")

    with pytest.raises(IntegrityError):
        with transaction.atomic():
            Country.objects.create(name="Brazil 3", iso2="B2", iso3="BRA")

    with pytest.raises(IntegrityError):
        with transaction.atomic():
            State.objects.create(country=country, name="Sao Paulo")

    with pytest.raises(IntegrityError):
        with transaction.atomic():
            City.objects.create(state=state, name="Sao Paulo")
