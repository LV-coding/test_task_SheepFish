from django.urls import path
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions

schema_view = get_schema_view(
    openapi.Info(
        title="Test task",
        default_version="v1",
        description="Test task for Python (Django) developer in SheepFish",
    ),
    permission_classes=(permissions.IsAuthenticatedOrReadOnly,),
    public=True,
)

swagger_pattern = path(
    "swagger/", schema_view.with_ui("swagger", cache_timeout=0), name="schema-swagger-ui"
)
