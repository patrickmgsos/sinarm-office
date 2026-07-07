"""Tests for case, document, workflow and status reference type models."""

from __future__ import annotations

import uuid

import pytest
from django.db import IntegrityError, transaction

from apps.common.models import ArchivableModel
from apps.reference_data.models import (
    CaseType,
    DocumentType,
    StatusType,
    WorkflowType,
)

pytestmark = pytest.mark.django_db


def test_reference_type_models_use_uuid_and_archive_status() -> None:
    """Reference type models should use UUID identity and archive semantics."""
    case_type = CaseType.objects.create(name="Acquisition", code="acquisition")
    document_type = DocumentType.objects.create(
        name="Identity Document",
        code="identity-document",
    )
    workflow_type = WorkflowType.objects.create(name="Default", code="default")
    status_type = StatusType.objects.create(name="Pending", code="pending")

    assert isinstance(case_type.id, uuid.UUID)
    assert document_type.status == ArchivableModel.ArchiveStatus.ACTIVE
    assert workflow_type.status == ArchivableModel.ArchiveStatus.ACTIVE
    assert status_type.status == ArchivableModel.ArchiveStatus.ACTIVE


def test_reference_type_uniqueness_constraints() -> None:
    """Each reference type table should enforce unique name and code."""
    CaseType.objects.create(name="Acquisition", code="acquisition")
    DocumentType.objects.create(name="Identity Document", code="identity-document")
    WorkflowType.objects.create(name="Default", code="default")
    StatusType.objects.create(name="Pending", code="pending")

    with pytest.raises(IntegrityError):
        with transaction.atomic():
            CaseType.objects.create(name="Acquisition", code="other")

    with pytest.raises(IntegrityError):
        with transaction.atomic():
            DocumentType.objects.create(name="Other", code="identity-document")

    with pytest.raises(IntegrityError):
        with transaction.atomic():
            WorkflowType.objects.create(name="Default", code="other")

    with pytest.raises(IntegrityError):
        with transaction.atomic():
            StatusType.objects.create(name="Other", code="pending")
