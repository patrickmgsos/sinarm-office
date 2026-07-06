"""Health check URLs."""

from __future__ import annotations

from django.urls import path

from apps.health import views

app_name = "health"

urlpatterns = [
    path("health/", views.health_check, name="health"),
    path("health/db/", views.database_health_check, name="health-db"),
    path("health/redis/", views.redis_health_check, name="health-redis"),
    path("health/celery/", views.celery_health_check, name="health-celery"),
    path("health/storage/", views.storage_health_check, name="health-storage"),
]
