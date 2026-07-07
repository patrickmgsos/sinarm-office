"""Tests for case, document, workflow and status reference type services."""

from __future__ import annotations

import pytest

from apps.common.models import ArchivableModel
from apps.reference_data.services import (
    archive_case_type,
    archive_document_type,
    archive_status_type,
    archive_workflow_type,
    create_case_type,
    create_document_type,
    create_status_type,
    create_workflow_type,
)

pytestmark = pytest.mark.django_db


def test_create_reference_type_services() -> None:
    """Services should create reference type records only."""
    case_type = create_case_type(
        name="Acquisition",
        code="acquisition",
        description="Reference case type",
        is_system=True,
    )
    document_type = create_document_type(
        name="Identity Document",
        code="identity-document",
    )
    workflow_type = create_workflow_type(name="Default", code="default")
    status_type = create_status_type(name="Pending", code="pending")

    assert case_type.is_system is True
    assert document_type.code == "identity-document"
    assert workflow_type.name == "Default"
    assert status_type.code == "pending"


def test_archive_reference_type_services() -> None:
    """Archive services should preserve reference type history."""
    case_type = create_case_type(name="Acquisition", code="acquisition")
    document_type = create_document_type(
        name="Identity Document",
        code="identity-document",
    )
    workflow_type = create_workflow_type(name="Default", code="default")
    status_type = create_status_type(name="Pending", code="pending")

    archive_case_type(case_type)
    archive_document_type(document_type)
    archive_workflow_type(workflow_type)
    archive_status_type(status_type)

    assert case_type.status == ArchivableModel.ArchiveStatus.ARCHIVED
    assert document_type.status == ArchivableModel.ArchiveStatus.ARCHIVED
    assert workflow_type.status == ArchivableModel.ArchiveStatus.ARCHIVED
    assert status_type.status == ArchivableModel.ArchiveStatus.ARCHIVED
