"""Tests for audit application services."""

from __future__ import annotations

import uuid

import pytest
from django.contrib.auth import get_user_model
from django.test import RequestFactory

from apps.audit.models import AuditEvent
from apps.audit.services import record_audit_event, start_audit_session

pytestmark = pytest.mark.django_db


def test_record_audit_event_from_request() -> None:
    """Service should capture actor, IP and user agent from request."""
    user_model = get_user_model()
    actor = user_model.objects.create_user(
        username="service-audit-user",
        email="service-audit@example.com",
        password="test-pass",
    )
    request = RequestFactory().post(
        "/technical-action/",
        HTTP_USER_AGENT="pytest-agent",
        REMOTE_ADDR="127.0.0.1",
    )
    request.user = actor
    organization_id = uuid.uuid4()
    entity_id = uuid.uuid4()

    event = record_audit_event(
        action="updated",
        entity_type="platform.resource",
        entity_id=entity_id,
        organization_id=organization_id,
        metadata={"field": "value"},
        request=request,
    )

    assert AuditEvent.objects.count() == 1
    assert event.actor == actor
    assert event.organization_id == organization_id
    assert event.ip_address == "127.0.0.1"
    assert event.user_agent == "pytest-agent"


def test_start_audit_session_from_request() -> None:
    """Service should create an audit session with request metadata."""
    request = RequestFactory().get(
        "/login/",
        HTTP_USER_AGENT="pytest-agent",
        REMOTE_ADDR="127.0.0.1",
    )

    audit_session = start_audit_session(request=request, auth_method="password")

    assert audit_session.auth_method == "password"
    assert audit_session.ip_address == "127.0.0.1"
    assert audit_session.user_agent == "pytest-agent"
