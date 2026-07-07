"""Application services for technical identity records."""

from __future__ import annotations

import uuid
from collections.abc import Iterable, Mapping
from typing import Any

from django.contrib.auth import get_user_model
from django.db import transaction
from django.utils import timezone

from apps.common.models import ArchivableModel
from apps.identity.models import CustomUser, Permission, Role, UserRole, UserSession


@transaction.atomic
def create_user(
    *,
    username: str,
    email: str = "",
    password: str | None = None,
    display_name: str = "",
    organization_id: uuid.UUID | None = None,
    is_staff: bool = False,
    is_superuser: bool = False,
) -> CustomUser:
    """Create a Django-auth-compatible user."""
    user_model = get_user_model()
    user = user_model.objects.create_user(
        username=username,
        email=email,
        password=password,
        display_name=display_name,
        organization_id=organization_id,
        is_staff=is_staff,
        is_superuser=is_superuser,
    )
    return user


@transaction.atomic
def create_permission(
    *,
    code: str,
    name: str,
    description: str = "",
    is_active: bool = True,
) -> Permission:
    """Create a stable technical permission."""
    return Permission.objects.create(
        code=code,
        name=name,
        description=description,
        is_active=is_active,
    )


@transaction.atomic
def create_role(
    *,
    code: str,
    name: str,
    description: str = "",
    organization_id: uuid.UUID | None = None,
    permissions: Iterable[Permission] = (),
) -> Role:
    """Create a technical role and attach permissions."""
    role = Role.objects.create(
        code=code,
        name=name,
        description=description,
        organization_id=organization_id,
    )
    role.permissions.set(permissions)
    return role


@transaction.atomic
def assign_role(
    *,
    user: CustomUser,
    role: Role,
    organization_id: uuid.UUID | None = None,
    expires_at: Any | None = None,
) -> UserRole:
    """Assign a role to a user within an optional organization scope."""
    return UserRole.objects.create(
        user=user,
        role=role,
        organization_id=organization_id,
        expires_at=expires_at,
    )


@transaction.atomic
def archive_role(role: Role) -> Role:
    """Archive a role without deleting historical assignments."""
    role.status = ArchivableModel.ArchiveStatus.ARCHIVED
    role.archived_at = timezone.now()
    role.save(update_fields=["status", "archived_at", "updated_at"])
    return role


@transaction.atomic
def revoke_user_role(user_role: UserRole) -> UserRole:
    """Archive a role assignment without deleting it."""
    user_role.status = ArchivableModel.ArchiveStatus.ARCHIVED
    user_role.archived_at = timezone.now()
    user_role.save(update_fields=["status", "archived_at", "updated_at"])
    return user_role


@transaction.atomic
def start_user_session(
    *,
    user: CustomUser,
    session_key: str,
    organization_id: uuid.UUID | None = None,
    ip_address: str | None = None,
    user_agent: str = "",
    auth_method: str = "",
    metadata: Mapping[str, Any] | None = None,
) -> UserSession:
    """Create technical metadata for an authenticated session."""
    return UserSession.objects.create(
        user=user,
        organization_id=organization_id,
        session_key=session_key,
        ip_address=ip_address,
        user_agent=user_agent,
        auth_method=auth_method,
        metadata=dict(metadata or {}),
    )


@transaction.atomic
def end_user_session(user_session: UserSession) -> UserSession:
    """Mark a user session as ended."""
    user_session.status = UserSession.SessionStatus.ENDED
    user_session.ended_at = timezone.now()
    user_session.save(update_fields=["status", "ended_at", "updated_at"])
    return user_session


@transaction.atomic
def revoke_user_session(user_session: UserSession) -> UserSession:
    """Mark a user session as revoked."""
    user_session.status = UserSession.SessionStatus.REVOKED
    user_session.revoked_at = timezone.now()
    user_session.save(update_fields=["status", "revoked_at", "updated_at"])
    return user_session
