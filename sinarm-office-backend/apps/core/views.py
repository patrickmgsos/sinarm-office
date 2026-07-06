"""Infrastructure views for operational checks."""

from __future__ import annotations

from django.http import HttpRequest, JsonResponse
from django.views.decorators.http import require_GET


@require_GET
def health_check(request: HttpRequest) -> JsonResponse:
    """Return a minimal readiness response for the Django process."""
    return JsonResponse(
        {
            "status": "ok",
            "service": "sinarm-office-backend",
        }
    )
