"""Tests for technical audit models."""

from __future__ import annotations

import uuid

import pytest
from django.contrib.auth import get_user_model

from apps.audit.models import AuditEvent, AuditEventType, AuditSession

pytestmark = pytest.mark.django_db


def test_audit_event_type_uses_uuid_primary_key() -> None:
    """AuditEventType must use UUID identity from BaseModel."""
    event_type = AuditEventType.objects.create(
        code="platform.test",
        name="Platform Test",
    )

    assert isinstance(event_type.id, uuid.UUID)


def test_audit_event_records_actor_and_entity() -> None:
    """AuditEvent should preserve actor, optional organization and entity data."""
    user_model = get_user_model()
    actor = user_model.objects.create_user(
        username="audit-user",
        email="audit@example.com",
        password="test-pass",
    )
    organization_id = uuid.uuid4()
    entity_id = uuid.uuid4()
    event_type = AuditEventType.objects.create(
        code="platform.created",
        name="Platform Created",
    )
    audit_session = AuditSession.objects.create(
        actor=actor,
        organization_id=organization_id,
        ip_address="127.0.0.1",
        user_agent="pytest",
    )

    event = AuditEvent.objects.create(
        event_type=event_type,
        audit_session=audit_session,
        actor=actor,
        organization_id=organization_id,
        action="created",
        entity_type="platform.resource",
        entity_id=entity_id,
        metadata={"source": "test"},
        ip_address="127.0.0.1",
        user_agent="pytest",
    )

    assert event.actor == actor
    assert event.organization_id == organization_id
    assert event.entity_type == "platform.resource"
    assert event.entity_id == entity_id
    assert event.metadata == {"source": "test"}
