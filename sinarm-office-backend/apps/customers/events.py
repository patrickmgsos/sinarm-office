"""Customer domain events."""

from __future__ import annotations

import uuid
from dataclasses import dataclass
from datetime import datetime


@dataclass(frozen=True, slots=True)
class CustomerRegistered:
    """Event emitted when a customer is registered."""

    customer_id: uuid.UUID
    name: str
    document_type: str
    document_number: str
    occurred_at: datetime
