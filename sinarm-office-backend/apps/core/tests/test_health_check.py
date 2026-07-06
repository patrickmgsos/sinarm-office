"""Tests for operational health checks."""

from __future__ import annotations

from django.test import Client


def test_health_check_returns_ok(client: Client) -> None:
    """Health endpoint should confirm the Django process is ready."""
    response = client.get("/health/")

    assert response.status_code == 200
    assert response.json()["status"] == "ok"
