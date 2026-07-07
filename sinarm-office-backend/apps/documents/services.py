"""Document generation MVP services."""

from __future__ import annotations

import uuid
from dataclasses import dataclass

from django.conf import settings
from django.core.files.base import ContentFile
from django.template import Context, Template
from django.utils import timezone
from django.utils.text import slugify

from apps.cases.models import Case
from apps.common.exceptions import BusinessRuleViolation, NotFoundException
from apps.customers.models import Customer
from apps.documents.docx import build_docx
from apps.documents.models import GeneratedDocument


@dataclass(frozen=True, slots=True)
class GenerateDocumentData:
    """Input data for generating a DOCX document."""

    customer_id: uuid.UUID
    template_type: str
    case_id: uuid.UUID | None = None
    notes: str = ""


class GenerateDocumentService:
    """Generate simple DOCX documents for the MVP."""

    def execute(self, *, data: GenerateDocumentData) -> GeneratedDocument:
        """Generate a DOCX document and store it in media."""
        customer = Customer.objects.filter(id=data.customer_id).first()
        if customer is None:
            msg = "Customer was not found."
            raise NotFoundException(msg)

        case = None
        if data.case_id is not None:
            case = Case.objects.filter(id=data.case_id).first()
            if case is None:
                msg = "Case was not found."
                raise NotFoundException(msg)

        if data.template_type not in GeneratedDocument.TemplateType.values:
            msg = "Document template type is invalid."
            raise BusinessRuleViolation(msg)

        template_content = self._load_template(template_type=data.template_type)
        rendered = Template(template_content).render(
            Context(
                {
                    "customer": customer,
                    "case": case,
                    "today": timezone.localdate(),
                },
            ),
        )
        paragraphs = [line.strip() for line in rendered.splitlines() if line.strip()]
        docx_bytes = build_docx(paragraphs=paragraphs)
        title = GeneratedDocument.TemplateType(data.template_type).label
        filename = self._build_filename(
            customer=customer,
            template_type=data.template_type,
        )

        document = GeneratedDocument(
            customer=customer,
            case=case,
            template_type=data.template_type,
            title=title,
            notes=data.notes,
        )
        document.file.save(filename, ContentFile(docx_bytes), save=True)
        return document

    def _load_template(self, *, template_type: str) -> str:
        template_path = (
            settings.BASE_DIR
            / "apps"
            / "documents"
            / "templates"
            / "documents"
            / f"{template_type}.txt"
        )
        return template_path.read_text(encoding="utf-8")

    def _build_filename(self, *, customer: Customer, template_type: str) -> str:
        timestamp = timezone.now().strftime("%Y%m%d%H%M%S")
        customer_slug = slugify(customer.name) or "customer"
        return f"{template_type}-{customer_slug}-{timestamp}.docx"
