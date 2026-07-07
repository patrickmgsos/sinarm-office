"""Tests for case, document, workflow and status reference type selectors."""

from __future__ import annotations

import pytest

from apps.common.models import ArchivableModel
from apps.reference_data.selectors import (
    case_types_active,
    document_types_active,
    status_types_active,
    workflow_types_active,
)
from apps.reference_data.services import (
    create_case_type,
    create_document_type,
    create_status_type,
    create_workflow_type,
)

pytestmark = pytest.mark.django_db


def test_reference_type_active_selectors_exclude_archived_records() -> None:
    """Reference type selectors should return only active records."""
    case_type = create_case_type(name="Acquisition", code="acquisition")
    archived_case_type = create_case_type(name="Transfer", code="transfer")
    document_type = create_document_type(
        name="Identity Document",
        code="identity-document",
    )
    archived_document_type = create_document_type(
        name="Residence Proof",
        code="residence-proof",
    )
    workflow_type = create_workflow_type(name="Default", code="default")
    archived_workflow_type = create_workflow_type(name="Alternative", code="alt")
    status_type = create_status_type(name="Pending", code="pending")
    archived_status_type = create_status_type(name="Finished", code="finished")

    archived_case_type.status = ArchivableModel.ArchiveStatus.ARCHIVED
    archived_case_type.save(update_fields=["status"])
    archived_document_type.status = ArchivableModel.ArchiveStatus.ARCHIVED
    archived_document_type.save(update_fields=["status"])
    archived_workflow_type.status = ArchivableModel.ArchiveStatus.ARCHIVED
    archived_workflow_type.save(update_fields=["status"])
    archived_status_type.status = ArchivableModel.ArchiveStatus.ARCHIVED
    archived_status_type.save(update_fields=["status"])

    assert list(case_types_active()) == [case_type]
    assert list(document_types_active()) == [document_type]
    assert list(workflow_types_active()) == [workflow_type]
    assert list(status_types_active()) == [status_type]
