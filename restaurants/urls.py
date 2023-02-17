from django.contrib import admin
from django.urls import path, include
from restaurants.settings import DEBUG
from restaurants.swagger import swagger_pattern

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/v1/printers/", include("printers.api.v1.routes")),
    path("api/v1/checks/", include("checks.api.v1.routes")),
]

if DEBUG:
    urlpatterns.append(swagger_pattern)
