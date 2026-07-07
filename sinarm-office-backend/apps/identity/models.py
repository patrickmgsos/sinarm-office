"""Technical identity models for authentication and authorization."""

from __future__ import annotations

from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils import timezone

from apps.common.models import ArchivableModel, BaseModel


class CustomUser(BaseModel, AbstractUser):
    """Custom user compatible with Django authentication."""

    email = models.EmailField()
    display_name = models.CharField(max_length=180, blank=True)
    organization_id = models.UUIDField(blank=True, null=True, db_index=True)
    timezone = models.CharField(max_length=64, default="America/Sao_Paulo")
    locale = models.CharField(max_length=16, default="pt-br")
    last_seen_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=["email"],
                condition=~models.Q(email=""),
                name="ux_identity_user_email_not_blank",
            ),
        ]
        ordering = ["username"]
        verbose_name = "user"
        verbose_name_plural = "users"

    def __str__(self) -> str:
        """Return the best available user display label."""
        return self.display_name or self.get_username()


class Permission(BaseModel):
    """Stable technical permission code."""

    code = models.SlugField(max_length=140, unique=True)
    name = models.CharField(max_length=180)
    description = models.TextField(blank=True)
    is_active = models.BooleanField(default=True)

    class Meta:
        ordering = ["code"]
        verbose_name = "permission"
        verbose_name_plural = "permissions"

    def __str__(self) -> str:
        """Return the stable permission code."""
        return self.code


class Role(BaseModel, ArchivableModel):
    """Technical role grouping permissions for authorization."""

    code = models.SlugField(max_length=120)
    name = models.CharField(max_length=180)
    description = models.TextField(blank=True)
    organization_id = models.UUIDField(blank=True, null=True, db_index=True)
    permissions = models.ManyToManyField(
        Permission,
        blank=True,
        related_name="roles",
    )

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=["organization_id", "code"],
                name="ux_identity_role_organization_code",
            ),
            models.UniqueConstraint(
                fields=["code"],
                condition=models.Q(organization_id__isnull=True),
                name="ux_identity_role_global_code",
            ),
        ]
        ordering = ["code"]
        verbose_name = "role"
        verbose_name_plural = "roles"

    def __str__(self) -> str:
        """Return the stable role code."""
        return self.code


class UserRole(BaseModel, ArchivableModel):
    """Assignment of a role to a user within an optional organization scope."""

    user = models.ForeignKey(
        CustomUser,
        on_delete=models.CASCADE,
        related_name="role_assignments",
    )
    role = models.ForeignKey(
        Role,
        on_delete=models.PROTECT,
        related_name="user_assignments",
    )
    organization_id = models.UUIDField(blank=True, null=True, db_index=True)
    assigned_at = models.DateTimeField(default=timezone.now)
    expires_at = models.DateTimeField(blank=True, null=True)

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=["user", "role", "organization_id"],
                condition=models.Q(status=ArchivableModel.ArchiveStatus.ACTIVE),
                name="ux_identity_active_user_role_scope",
            ),
            models.UniqueConstraint(
                fields=["user", "role"],
                condition=(
                    models.Q(status=ArchivableModel.ArchiveStatus.ACTIVE)
                    & models.Q(organization_id__isnull=True)
                ),
                name="ux_identity_active_user_role_global",
            ),
        ]
        indexes = [
            models.Index(fields=["user", "status"]),
            models.Index(fields=["role", "status"]),
            models.Index(fields=["organization_id", "status"]),
        ]
        ordering = ["user__username", "role__code"]
        verbose_name = "user role"
        verbose_name_plural = "user roles"

    def __str__(self) -> str:
        """Return a compact assignment label."""
        return f"{self.user_id}:{self.role.code}"


class UserSession(BaseModel):
    """Technical session metadata for authenticated users."""

    class SessionStatus(models.TextChoices):
        ACTIVE = "active", "Active"
        ENDED = "ended", "Ended"
        REVOKED = "revoked", "Revoked"

    user = models.ForeignKey(
        CustomUser,
        on_delete=models.CASCADE,
        related_name="identity_sessions",
    )
    organization_id = models.UUIDField(blank=True, null=True, db_index=True)
    session_key = models.CharField(max_length=128, unique=True)
    ip_address = models.GenericIPAddressField(blank=True, null=True)
    user_agent = models.TextField(blank=True)
    auth_method = models.CharField(max_length=64, blank=True)
    status = models.CharField(
        max_length=32,
        choices=SessionStatus.choices,
        default=SessionStatus.ACTIVE,
    )
    started_at = models.DateTimeField(default=timezone.now)
    ended_at = models.DateTimeField(blank=True, null=True)
    revoked_at = models.DateTimeField(blank=True, null=True)
    metadata = models.JSONField(default=dict, blank=True)

    class Meta:
        indexes = [
            models.Index(fields=["user", "started_at"]),
            models.Index(fields=["organization_id", "started_at"]),
            models.Index(fields=["status", "started_at"]),
        ]
        ordering = ["-started_at"]
        verbose_name = "user session"
        verbose_name_plural = "user sessions"

    def __str__(self) -> str:
        """Return a compact session label."""
        return f"identity-session:{self.user_id}:{self.started_at.isoformat()}"
