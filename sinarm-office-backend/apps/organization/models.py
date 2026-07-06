"""Technical organization models for future multi-company support."""

from __future__ import annotations

from django.db import models

from apps.common.models import ArchivableModel, BaseModel


class Organization(BaseModel, ArchivableModel):
    """Root organization for future multi-company operation."""

    name = models.CharField(max_length=180)
    legal_name = models.CharField(max_length=220, blank=True)
    document_number = models.CharField(max_length=32, blank=True)
    email = models.EmailField(blank=True)
    phone = models.CharField(max_length=32, blank=True)
    is_default = models.BooleanField(default=False)

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=["document_number"],
                condition=~models.Q(document_number=""),
                name="ux_organization_document_number_not_blank",
            ),
        ]
        ordering = ["name"]
        verbose_name = "organization"
        verbose_name_plural = "organizations"

    def __str__(self) -> str:
        """Return organization display name."""
        return self.name


class Office(BaseModel, ArchivableModel):
    """Physical or operational office/branch of an organization."""

    organization = models.ForeignKey(
        Organization,
        on_delete=models.PROTECT,
        related_name="offices",
    )
    name = models.CharField(max_length=180)
    code = models.SlugField(max_length=80)
    email = models.EmailField(blank=True)
    phone = models.CharField(max_length=32, blank=True)
    is_headquarters = models.BooleanField(default=False)

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=["organization", "code"],
                name="ux_office_organization_code",
            ),
        ]
        ordering = ["organization__name", "name"]
        verbose_name = "office"
        verbose_name_plural = "offices"

    def __str__(self) -> str:
        """Return office display name."""
        return f"{self.organization.name} - {self.name}"


class Department(BaseModel, ArchivableModel):
    """Internal department within an organization and optional office."""

    organization = models.ForeignKey(
        Organization,
        on_delete=models.PROTECT,
        related_name="departments",
    )
    office = models.ForeignKey(
        Office,
        blank=True,
        null=True,
        on_delete=models.PROTECT,
        related_name="departments",
    )
    name = models.CharField(max_length=180)
    code = models.SlugField(max_length=80)
    description = models.TextField(blank=True)

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=["organization", "code"],
                name="ux_department_organization_code",
            ),
        ]
        ordering = ["organization__name", "name"]
        verbose_name = "department"
        verbose_name_plural = "departments"

    def __str__(self) -> str:
        """Return department display name."""
        return f"{self.organization.name} - {self.name}"
