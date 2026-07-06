"""Operational health check views."""

from __future__ import annotations

from django.conf import settings
from django.core.cache import cache
from django.core.files.storage import default_storage
from django.db import connections
from django.db.utils import DatabaseError
from django.http import HttpRequest, JsonResponse
from django.views.decorators.http import require_GET


def _health_response(component: str, status: str, **details: str) -> JsonResponse:
    """Build a consistent JSON response for health endpoints."""
    status_code = 200 if status == "ok" else 503
    payload = {"component": component, "status": status, **details}
    return JsonResponse(payload, status=status_code)


@require_GET
def health_check(request: HttpRequest) -> JsonResponse:
    """Return a minimal liveness response for the Django process."""
    return _health_response("application", "ok", service="sinarm-office-backend")


@require_GET
def database_health_check(request: HttpRequest) -> JsonResponse:
    """Check whether the default database connection is available."""
    try:
        connections["default"].ensure_connection()
    except DatabaseError:
        return _health_response("database", "unavailable")

    return _health_response("database", "ok")


@require_GET
def redis_health_check(request: HttpRequest) -> JsonResponse:
    """Check whether the configured cache backend is reachable."""
    cache_key = "sinarm-office-health-check"

    try:
        cache.set(cache_key, "ok", timeout=5)
        cache.get(cache_key)
    except Exception:
        return _health_response("redis", "unavailable")

    return _health_response("redis", "ok")


@require_GET
def celery_health_check(request: HttpRequest) -> JsonResponse:
    """Confirm that Celery settings are present."""
    broker_url = getattr(settings, "CELERY_BROKER_URL", "")
    status = "ok" if broker_url else "unavailable"
    return _health_response("celery", status)


@require_GET
def storage_health_check(request: HttpRequest) -> JsonResponse:
    """Confirm that the default storage can be accessed."""
    try:
        default_storage.exists(".healthcheck")
    except Exception:
        return _health_response("storage", "unavailable")

    return _health_response("storage", "ok")
