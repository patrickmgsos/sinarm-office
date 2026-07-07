"""Tests for geographic reference data selectors."""

from __future__ import annotations

import pytest

from apps.common.models import ArchivableModel
from apps.reference_data.selectors import (
    cities_for_state,
    countries_active,
    states_for_country,
)
from apps.reference_data.services import create_city, create_country, create_state

pytestmark = pytest.mark.django_db


def test_countries_active_excludes_archived_records() -> None:
    """Country selector should return only active countries."""
    active = create_country(name="Brazil", iso2="BR", iso3="BRA")
    archived = create_country(name="Argentina", iso2="AR", iso3="ARG")
    archived.status = ArchivableModel.ArchiveStatus.ARCHIVED
    archived.save(update_fields=["status"])

    assert list(countries_active()) == [active]


def test_states_and_cities_selectors_filter_scope() -> None:
    """Geographic selectors should filter by country and state."""
    country = create_country(name="Brazil", iso2="BR", iso3="BRA")
    other_country = create_country(name="Argentina", iso2="AR", iso3="ARG")
    state = create_state(country=country, name="Sao Paulo", code="SP")
    other_state = create_state(country=other_country, name="Buenos Aires")
    city = create_city(state=state, name="Sao Paulo", ibge_code="3550308")
    create_city(state=other_state, name="Buenos Aires")

    assert list(states_for_country(country_id=country.id)) == [state]
    assert list(cities_for_state(state_id=state.id)) == [city]
