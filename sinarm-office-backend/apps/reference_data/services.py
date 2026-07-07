"""Application services for firearm reference data."""

from __future__ import annotations

from django.db import transaction
from django.utils import timezone

from apps.common.models import ArchivableModel
from apps.reference_data.models import (
    Caliber,
    City,
    Country,
    FirearmModel,
    Manufacturer,
    State,
)


@transaction.atomic
def create_manufacturer(
    *,
    name: str,
    country: str = "",
    notes: str = "",
) -> Manufacturer:
    """Create a firearm manufacturer reference record."""
    return Manufacturer.objects.create(name=name, country=country, notes=notes)


@transaction.atomic
def create_caliber(
    *,
    name: str,
    category: str = "",
    description: str = "",
) -> Caliber:
    """Create a caliber reference record."""
    return Caliber.objects.create(
        name=name,
        category=category,
        description=description,
    )


@transaction.atomic
def create_firearm_model(
    *,
    manufacturer: Manufacturer,
    name: str,
    caliber: Caliber | None = None,
    species: str = "",
    operation: str = "",
    notes: str = "",
) -> FirearmModel:
    """Create firearm model reference data without creating a Firearm."""
    return FirearmModel.objects.create(
        manufacturer=manufacturer,
        name=name,
        caliber=caliber,
        species=species,
        operation=operation,
        notes=notes,
    )


@transaction.atomic
def archive_manufacturer(manufacturer: Manufacturer) -> Manufacturer:
    """Archive a manufacturer without deleting reference history."""
    manufacturer.status = ArchivableModel.ArchiveStatus.ARCHIVED
    manufacturer.archived_at = timezone.now()
    manufacturer.save(update_fields=["status", "archived_at", "updated_at"])
    return manufacturer


@transaction.atomic
def archive_caliber(caliber: Caliber) -> Caliber:
    """Archive a caliber without deleting reference history."""
    caliber.status = ArchivableModel.ArchiveStatus.ARCHIVED
    caliber.archived_at = timezone.now()
    caliber.save(update_fields=["status", "archived_at", "updated_at"])
    return caliber


@transaction.atomic
def archive_firearm_model(firearm_model: FirearmModel) -> FirearmModel:
    """Archive a firearm model without deleting reference history."""
    firearm_model.status = ArchivableModel.ArchiveStatus.ARCHIVED
    firearm_model.archived_at = timezone.now()
    firearm_model.save(update_fields=["status", "archived_at", "updated_at"])
    return firearm_model


@transaction.atomic
def create_country(
    *,
    name: str,
    iso2: str,
    iso3: str,
    phone_code: str = "",
) -> Country:
    """Create a country reference record."""
    return Country.objects.create(
        name=name,
        iso2=iso2,
        iso3=iso3,
        phone_code=phone_code,
    )


@transaction.atomic
def create_state(
    *,
    country: Country,
    name: str,
    code: str = "",
) -> State:
    """Create a state reference record."""
    return State.objects.create(country=country, name=name, code=code)


@transaction.atomic
def create_city(
    *,
    state: State,
    name: str,
    ibge_code: str = "",
) -> City:
    """Create a city reference record."""
    return City.objects.create(state=state, name=name, ibge_code=ibge_code)


@transaction.atomic
def archive_country(country: Country) -> Country:
    """Archive a country without deleting reference history."""
    country.status = ArchivableModel.ArchiveStatus.ARCHIVED
    country.archived_at = timezone.now()
    country.save(update_fields=["status", "archived_at", "updated_at"])
    return country


@transaction.atomic
def archive_state(state: State) -> State:
    """Archive a state without deleting reference history."""
    state.status = ArchivableModel.ArchiveStatus.ARCHIVED
    state.archived_at = timezone.now()
    state.save(update_fields=["status", "archived_at", "updated_at"])
    return state


@transaction.atomic
def archive_city(city: City) -> City:
    """Archive a city without deleting reference history."""
    city.status = ArchivableModel.ArchiveStatus.ARCHIVED
    city.archived_at = timezone.now()
    city.save(update_fields=["status", "archived_at", "updated_at"])
    return city
