"""Customer registration specifications."""

from __future__ import annotations

from apps.customers.models import Customer


class CustomerCanBeRegisteredSpecification:
    """Specification for minimum customer registration data."""

    def is_satisfied_by(
        self,
        *,
        name: str,
        kind: str,
        document_type: str,
        document_number: str,
    ) -> bool:
        """Return whether registration data has the required shape."""
        if not name.strip():
            return False
        if kind not in Customer.CustomerKind.values:
            return False
        if document_type not in Customer.DocumentType.values:
            return False
        if not document_number.isdigit():
            return False
        if document_type == Customer.DocumentType.CPF:
            return len(document_number) == 11
        if document_type == Customer.DocumentType.CNPJ:
            return len(document_number) == 14

        return False
