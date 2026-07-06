"""Root URL configuration for SINARM Office."""

from __future__ import annotations

from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path
from drf_spectacular.views import SpectacularAPIView, SpectacularSwaggerView

urlpatterns = [
    path("", include("apps.core.urls")),
    path("admin/", admin.site.urls),
    path("api/schema/", SpectacularAPIView.as_view(), name="schema"),
    path(
        "api/docs/",
        SpectacularSwaggerView.as_view(url_name="schema"),
        name="swagger-ui",
    ),
    path("api/accounts/", include("apps.accounts.urls")),
    path("api/clientes/", include("apps.clientes.urls")),
    path("api/armas/", include("apps.armas.urls")),
    path("api/processos/", include("apps.processos.urls")),
    path("api/documentos/", include("apps.documentos.urls")),
    path("api/modelos/", include("apps.modelos.urls")),
    path("api/auditoria/", include("apps.auditoria.urls")),
    path("api/workflows/", include("apps.workflows.urls")),
    path("api/ia/", include("apps.ia.urls")),
    path("api/dashboard/", include("apps.dashboard.urls")),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
