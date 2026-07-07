"""Tests for Document generation MVP."""

from __future__ import annotations

import zipfile
from pathlib import Path

import pytest
from django.test import override_settings

from apps.common.exceptions import BusinessRuleViolation
from apps.customers.models import Customer
from apps.customers.services import RegisterNewCustomerService
from apps.documents.models import GeneratedDocument
from apps.documents.services import GenerateDocumentData, GenerateDocumentService

pytestmark = pytest.mark.django_db


def _register_customer() -> Customer:
    return (
        RegisterNewCustomerService()
        .execute(
            name="Ada Lovelace",
            kind=Customer.CustomerKind.INDIVIDUAL,
            document_type=Customer.DocumentType.CPF,
            document_number="12345678901",
        )
        .customer
    )


def test_generate_renewal_need_docx(tmp_path: Path) -> None:
    """Document MVP should generate a DOCX file in media."""
    customer = _register_customer()

    with override_settings(MEDIA_ROOT=tmp_path):
        document = GenerateDocumentService().execute(
            data=GenerateDocumentData(
                customer_id=customer.id,
                template_type=GeneratedDocument.TemplateType.RENEWAL_NEED,
            ),
        )

        assert document.file.name.endswith(".docx")
        assert document.file.storage.exists(document.file.name)
        with zipfile.ZipFile(document.file.path) as docx:
            xml = docx.read("word/document.xml").decode()

    assert "Ada Lovelace" in xml
    assert "EFETIVA NECESSIDADE" in xml


def test_generate_document_rejects_invalid_template() -> None:
    """Document MVP should reject unknown template types."""
    customer = _register_customer()

    with pytest.raises(BusinessRuleViolation):
        GenerateDocumentService().execute(
            data=GenerateDocumentData(
                customer_id=customer.id,
                template_type="invalid",
            ),
        )
