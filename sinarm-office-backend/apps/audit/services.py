"""Application services for technical audit records."""

from __future__ import annotations

import uuid
from collections.abc import Mapping
from typing import Any

from django.contrib.auth import get_user_model
from django.db import transaction
from django.http import HttpRequest
from django.utils import timezone

from apps.audit.models import AuditEvent, AuditEventType, AuditSession

UserModel = get_user_model()


def get_client_ip(request: HttpRequest | None) -> str:
    """Extract the best-effort client IP from a request."""
    if request is None:
        return ""

    forwarded_for = str(request.META.get("HTTP_X_FORWARDED_FOR", ""))
    if forwarded_for:
        return forwarded_for.split(",")[0].strip()

    return str(request.META.get("REMOTE_ADDR", ""))


def get_user_agent(request: HttpRequest | None) -> str:
    """Extract the user agent from a request."""
    if request is None:
        return ""

    return str(request.META.get("HTTP_USER_AGENT", ""))


def get_request_actor(request: HttpRequest | None) -> Any | None:
    """Return the authenticated request user when available."""
    if request is None:
        return None

    user = getattr(request, "user", None)
    if user is not None and getattr(user, "is_authenticated", False):
        return user

    return None


@transaction.atomic
def start_audit_session(
    *,
    actor: Any | None = None,
    organization_id: uuid.UUID | None = None,
    request: HttpRequest | None = None,
    auth_method: str = "",
    metadata: Mapping[str, Any] | None = None,
) -> AuditSession:
    """Create an audit session for a user or operational activity."""
    request_actor = get_request_actor(request)
    resolved_actor = actor or request_actor

    return AuditSession.objects.create(
        actor=resolved_actor,
        organization_id=organization_id,
        session_key=getattr(getattr(request, "session", None), "session_key", "") or "",
        ip_address=get_client_ip(request) or None,
        user_agent=get_user_agent(request),
        auth_method=auth_method,
        metadata=dict(metadata or {}),
    )


@transaction.atomic
def end_audit_session(audit_session: AuditSession) -> AuditSession:
    """Mark an audit session as ended."""
    audit_session.ended_at = timezone.now()
    audit_session.save(update_fields=["ended_at", "updated_at"])
    return audit_session


@transaction.atomic
def record_audit_event(
    *,
    action: str,
    entity_type: str,
    entity_id: uuid.UUID | None = None,
    event_type: AuditEventType | None = None,
    audit_session: AuditSession | None = None,
    actor: Any | None = None,
    organization_id: uuid.UUID | None = None,
    metadata: Mapping[str, Any] | None = None,
    before_data: Mapping[str, Any] | None = None,
    after_data: Mapping[str, Any] | None = None,
    request: HttpRequest | None = None,
) -> AuditEvent:
    """Record an immutable technical audit event."""
    request_actor = get_request_actor(request)
    resolved_actor = actor or request_actor

    return AuditEvent.objects.create(
        event_type=event_type,
        audit_session=audit_session,
        actor=resolved_actor,
        organization_id=organization_id,
        action=action,
        entity_type=entity_type,
        entity_id=entity_id,
        metadata=dict(metadata or {}),
        before_data=dict(before_data) if before_data is not None else None,
        after_data=dict(after_data) if after_data is not None else None,
        ip_address=get_client_ip(request) or None,
        user_agent=get_user_agent(request),
    )
