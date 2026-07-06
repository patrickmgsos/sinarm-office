"""Tests for audit selectors."""

from __future__ import annotations

import uuid

import pytest

from apps.audit.models import AuditEvent, AuditEventType
from apps.audit.selectors import (
    audit_event_types_active,
    audit_events_for_entity,
)

pytestmark = pytest.mark.django_db


def test_audit_event_types_active_filters_inactive_types() -> None:
    """Selector should only return active event types."""
    active = AuditEventType.objects.create(code="active.event", name="Active")
    AuditEventType.objects.create(
        code="inactive.event",
        name="Inactive",
        is_active=False,
    )

    assert list(audit_event_types_active()) == [active]


def test_audit_events_for_entity_filters_by_entity() -> None:
    """Selector should return events for a specific audited entity."""
    entity_id = uuid.uuid4()
    expected = AuditEvent.objects.create(
        action="created",
        entity_type="platform.resource",
        entity_id=entity_id,
    )
    AuditEvent.objects.create(
        action="created",
        entity_type="platform.resource",
        entity_id=uuid.uuid4(),
    )

    assert list(
        audit_events_for_entity(
            entity_type="platform.resource",
            entity_id=entity_id,
        )
    ) == [expected]
