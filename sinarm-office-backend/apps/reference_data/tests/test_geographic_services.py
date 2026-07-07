"""Tests for geographic reference data services."""

from __future__ import annotations

import pytest

from apps.common.models import ArchivableModel
from apps.reference_data.services import (
    archive_city,
    archive_country,
    archive_state,
    create_city,
    create_country,
    create_state,
)

pytestmark = pytest.mark.django_db


def test_create_geographic_reference_data_services() -> None:
    """Services should create geographic reference records."""
    country = create_country(
        name="Brazil",
        iso2="BR",
        iso3="BRA",
        phone_code="+55",
    )
    state = create_state(country=country, name="Sao Paulo", code="SP")
    city = create_city(state=state, name="Sao Paulo", ibge_code="3550308")

    assert country.iso2 == "BR"
    assert state.country == country
    assert city.state == state


def test_archive_geographic_reference_data_services() -> None:
    """Archive services should preserve geographic reference data history."""
    country = create_country(name="Brazil", iso2="BR", iso3="BRA")
    state = create_state(country=country, name="Sao Paulo", code="SP")
    city = create_city(state=state, name="Sao Paulo")

    archive_country(country)
    archive_state(state)
    archive_city(city)

    assert country.status == ArchivableModel.ArchiveStatus.ARCHIVED
    assert state.status == ArchivableModel.ArchiveStatus.ARCHIVED
    assert city.status == ArchivableModel.ArchiveStatus.ARCHIVED
