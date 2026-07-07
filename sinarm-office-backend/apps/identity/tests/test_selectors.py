"""Tests for identity selectors."""

from __future__ import annotations

import uuid

import pytest

from apps.common.models import ArchivableModel
from apps.identity.models import Permission, Role, UserRole, UserSession
from apps.identity.selectors import (
    active_sessions_for_user,
    permissions_active,
    roles_active,
    roles_for_user,
    users_active,
)
from apps.identity.services import create_user

pytestmark = pytest.mark.django_db


def test_users_active_filters_inactive_users() -> None:
    """Selector should only return active users."""
    active = create_user(username="active-user")
    inactive = create_user(username="inactive-user-2")
    inactive.is_active = False
    inactive.save(update_fields=["is_active"])

    assert list(users_active()) == [active]


def test_permissions_active_filters_inactive_permissions() -> None:
    """Selector should only return active permissions."""
    active = Permission.objects.create(code="active.permission", name="Active")
    Permission.objects.create(
        code="inactive.permission",
        name="Inactive",
        is_active=False,
    )

    assert list(permissions_active()) == [active]


def test_roles_active_returns_global_and_scoped_roles() -> None:
    """Selector should return active roles for the requested scope."""
    organization_id = uuid.uuid4()
    global_role = Role.objects.create(code="global", name="Global")
    scoped_role = Role.objects.create(
        code="scoped",
        name="Scoped",
        organization_id=organization_id,
    )
    Role.objects.create(
        code="archived",
        name="Archived",
        status=ArchivableModel.ArchiveStatus.ARCHIVED,
    )

    assert list(roles_active(organization_id=organization_id)) == [
        global_role,
        scoped_role,
    ]


def test_roles_for_user_returns_active_assignments() -> None:
    """Selector should return only active roles for a user."""
    user = create_user(username="role-user")
    expected = Role.objects.create(code="expected", name="Expected")
    archived = Role.objects.create(code="old", name="Old")
    UserRole.objects.create(user=user, role=expected)
    UserRole.objects.create(
        user=user,
        role=archived,
        status=ArchivableModel.ArchiveStatus.ARCHIVED,
    )

    assert list(roles_for_user(user_id=user.id)) == [expected]


def test_active_sessions_for_user_filters_status() -> None:
    """Selector should return active sessions for the requested user."""
    user = create_user(username="session-selector-user")
    active = UserSession.objects.create(user=user, session_key="active-session")
    UserSession.objects.create(
        user=user,
        session_key="ended-session",
        status=UserSession.SessionStatus.ENDED,
    )

    assert list(active_sessions_for_user(user_id=user.id)) == [active]
