from printers.models import Printer
from printers.api.v1.serializer import PrinterSerializer

from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.filters import OrderingFilter, SearchFilter

from django_filters.rest_framework import DjangoFilterBackend


class PrinterListViewSet(ListCreateAPIView):
    """View for create and list views Printer API endpoint."""
    queryset = Printer.objects.all()
    serializer_class = PrinterSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields = ("check_type", "point_id")

    def get(self, request, *args, **kwargs):
        """GET method of the API."""
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        """POST method of the API."""
        return self.create(request, *args, **kwargs)


class PrinterViewSet(RetrieveUpdateDestroyAPIView):
    """View for create, update, delete and view single Printer API endpoint."""
    queryset = Printer.objects.all()
    serializer_class = PrinterSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]


    def get(self, request, *args, **kwargs):
        """GET method of the API."""
        return self.retrieve(request, *args, **kwargs)

    def put(self, request, *args, **kwargs):
        """PUT method of the API."""
        return self.update(request, *args, **kwargs)

    def patch(self, request, *args, **kwargs):
        """PATCH method of the API."""
        return self.partial_update(request, *args, **kwargs)

    def delete(self, request, *args, **kwargs):
        """DELETE method of the API."""
        return self.destroy(request, *args, **kwargs)
