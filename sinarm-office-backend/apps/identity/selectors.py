"""Query helpers for technical identity records."""

from __future__ import annotations

import uuid

from django.db.models import Q, QuerySet

from apps.common.models import ArchivableModel
from apps.identity.models import CustomUser, Permission, Role, UserRole, UserSession


def users_active() -> QuerySet[CustomUser]:
    """Return active users ordered by username."""
    return CustomUser.objects.filter(is_active=True).order_by("username")


def permissions_active() -> QuerySet[Permission]:
    """Return active technical permissions."""
    return Permission.objects.filter(is_active=True).order_by("code")


def roles_active(
    *,
    organization_id: uuid.UUID | None = None,
    include_global: bool = True,
) -> QuerySet[Role]:
    """Return active roles for an optional organization scope."""
    queryset = Role.objects.filter(status=ArchivableModel.ArchiveStatus.ACTIVE)
    if organization_id is not None and include_global:
        queryset = queryset.filter(
            Q(organization_id=organization_id) | Q(organization_id__isnull=True),
        )
    elif organization_id is not None:
        queryset = queryset.filter(organization_id=organization_id)
    else:
        queryset = queryset.filter(organization_id__isnull=True)

    return queryset.prefetch_related("permissions").order_by("code")


def roles_for_user(
    *,
    user_id: uuid.UUID,
    organization_id: uuid.UUID | None = None,
) -> QuerySet[Role]:
    """Return active roles assigned to a user."""
    assignments = UserRole.objects.filter(
        user_id=user_id,
        status=ArchivableModel.ArchiveStatus.ACTIVE,
    )
    if organization_id is not None:
        assignments = assignments.filter(
            Q(organization_id=organization_id) | Q(organization_id__isnull=True),
        )

    return (
        Role.objects.filter(user_assignments__in=assignments)
        .distinct()
        .order_by("code")
    )


def active_sessions_for_user(*, user_id: uuid.UUID) -> QuerySet[UserSession]:
    """Return active identity sessions for a user."""
    return UserSession.objects.filter(
        user_id=user_id,
        status=UserSession.SessionStatus.ACTIVE,
    ).order_by("-started_at")
