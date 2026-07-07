"""Tests for identity services."""

from __future__ import annotations

import pytest

from apps.common.models import ArchivableModel
from apps.identity.models import UserSession
from apps.identity.services import (
    archive_role,
    assign_role,
    create_permission,
    create_role,
    create_user,
    end_user_session,
    revoke_user_role,
    revoke_user_session,
    start_user_session,
)

pytestmark = pytest.mark.django_db


def test_create_user_permission_role_and_assignment_services() -> None:
    """Services should create users, permissions, roles and assignments."""
    user = create_user(
        username="service-user",
        email="service@example.com",
        password="test-pass",
    )
    permission = create_permission(code="identity.manage", name="Manage identity")
    role = create_role(code="manager", name="Manager", permissions=[permission])
    assignment = assign_role(user=user, role=role)

    assert user.check_password("test-pass") is True
    assert list(role.permissions.all()) == [permission]
    assert assignment.user == user
    assert assignment.role == role


def test_archive_role_and_revoke_assignment_services() -> None:
    """Archive services should preserve role history."""
    user = create_user(username="archive-user")
    role = create_role(code="auditor", name="Auditor")
    assignment = assign_role(user=user, role=role)

    archive_role(role)
    revoke_user_role(assignment)

    assert role.status == ArchivableModel.ArchiveStatus.ARCHIVED
    assert assignment.status == ArchivableModel.ArchiveStatus.ARCHIVED


def test_user_session_lifecycle_services() -> None:
    """Session services should mark sessions as ended or revoked."""
    user = create_user(username="session-service-user")
    session = start_user_session(
        user=user,
        session_key="service-session",
        ip_address="127.0.0.1",
        user_agent="pytest",
        auth_method="password",
    )

    end_user_session(session)
    assert session.status == UserSession.SessionStatus.ENDED
    assert session.ended_at is not None

    revoked = start_user_session(user=user, session_key="revoked-session")
    revoke_user_session(revoked)
    assert revoked.status == UserSession.SessionStatus.REVOKED
    assert revoked.revoked_at is not None
