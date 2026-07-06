"""Abstract model foundations shared by future domain apps."""

from __future__ import annotations

import uuid

from django.db import models


class BaseModel(models.Model):
    """Base model for persistent entities with UUID identity and timestamps."""

    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True
