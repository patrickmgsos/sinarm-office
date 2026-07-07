"""Tests for technical identity models."""

from __future__ import annotations

import uuid

import pytest
from django.contrib.auth import get_user_model

from apps.common.models import ArchivableModel
from apps.identity.models import Permission, Role, UserRole, UserSession

pytestmark = pytest.mark.django_db


def test_custom_user_uses_uuid_and_django_auth_manager() -> None:
    """CustomUser must use UUID identity and remain compatible with Django auth."""
    user_model = get_user_model()
    user = user_model.objects.create_user(
        username="identity-user",
        email="identity@example.com",
        password="test-pass",
    )

    assert isinstance(user.id, uuid.UUID)
    assert user.check_password("test-pass") is True
    assert user.get_username() == "identity-user"


def test_role_permission_and_assignment_models() -> None:
    """Role assignments should connect users to technical permissions."""
    user_model = get_user_model()
    user = user_model.objects.create_user(username="operator")
    permission = Permission.objects.create(
        code="identity.view",
        name="View identity",
    )
    role = Role.objects.create(code="operator", name="Operator")
    role.permissions.add(permission)
    assignment = UserRole.objects.create(user=user, role=role)

    assert role.status == ArchivableModel.ArchiveStatus.ACTIVE
    assert list(role.permissions.all()) == [permission]
    assert assignment.user == user
    assert assignment.role == role


def test_user_session_records_authentication_metadata() -> None:
    """UserSession should store technical session data."""
    user_model = get_user_model()
    user = user_model.objects.create_user(username="session-user")
    session = UserSession.objects.create(
        user=user,
        session_key="session-key",
        ip_address="127.0.0.1",
        user_agent="pytest",
        auth_method="password",
    )

    assert session.user == user
    assert session.status == UserSession.SessionStatus.ACTIVE
    assert session.ip_address == "127.0.0.1"
