from django.urls import path
from printers.api.v1.views import PrinterListViewSet, PrinterViewSet

urlpatterns = [
    path("", PrinterListViewSet.as_view(), name="printers"),
    path("<int:pk>", PrinterViewSet.as_view(), name="printer")
]
