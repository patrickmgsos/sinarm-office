"""Tests for abstract model foundations."""

from __future__ import annotations

from django.db import models

from apps.core.models import BaseModel


def test_base_model_is_abstract_with_uuid_primary_key() -> None:
    """BaseModel must remain reusable without creating its own table."""
    id_field = BaseModel._meta.get_field("id")

    assert BaseModel._meta.abstract is True
    assert isinstance(id_field, models.UUIDField)
    assert id_field.primary_key is True
