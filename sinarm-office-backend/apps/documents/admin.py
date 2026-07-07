"""Django admin configuration for Document MVP."""

from __future__ import annotations

from typing import TYPE_CHECKING, TypeAlias

from django.contrib import admin, messages
from django.db import models
from django.http import HttpRequest

from apps.documents.models import GeneratedDocument
from apps.documents.services import GenerateDocumentData, GenerateDocumentService

if TYPE_CHECKING:
    GeneratedDocumentAdminBase: TypeAlias = admin.ModelAdmin[GeneratedDocument]  # noqa: UP040
else:
    GeneratedDocumentAdminBase = admin.ModelAdmin


@admin.register(GeneratedDocument)
class GeneratedDocumentAdmin(GeneratedDocumentAdminBase):
    """Admin for generated DOCX documents."""

    list_display = (
        "customer",
        "case",
        "template_type",
        "title",
        "generated_at",
        "status",
    )
    list_filter = ("status", "template_type", "generated_at")
    search_fields = ("customer__name", "customer__document_number", "title", "notes")
    autocomplete_fields = ("customer", "case")
    readonly_fields = ("id", "generated_at", "created_at", "updated_at")
    actions = ("regenerate_documents",)

    @admin.action(description="Regenerate selected DOCX files")
    def regenerate_documents(
        self,
        request: HttpRequest,
        queryset: models.QuerySet[GeneratedDocument],
    ) -> None:
        """Regenerate selected document files from editable templates."""
        service = GenerateDocumentService()
        regenerated = 0
        for document in queryset:
            service.execute(
                data=GenerateDocumentData(
                    customer_id=document.customer_id,
                    case_id=document.case_id,
                    template_type=document.template_type,
                    notes=document.notes,
                ),
            )
            regenerated += 1
        self.message_user(
            request,
            f"{regenerated} document(s) regenerated.",
            level=messages.SUCCESS,
        )
