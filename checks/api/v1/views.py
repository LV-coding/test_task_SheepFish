from checks.models import Check
from checks.api.v1.serializer import CreateCheckSerializer, CheckSerializer

from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView, CreateAPIView, ListAPIView
from rest_framework.permissions import IsAuthenticatedOrReadOnly
from rest_framework.filters import OrderingFilter, SearchFilter

from django_filters.rest_framework import DjangoFilterBackend


class CreateCheckViewSet(CreateAPIView):
    """View for create Check API endpoint."""
    queryset = Check.objects.all()
    serializer_class = CreateCheckSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]

    def post(self, request, *args, **kwargs):
        """POST method of the API."""
        return self.create(request, *args, **kwargs)


class CheckListViewSet(ListAPIView):
    """View for list views Check API endpoint."""
    queryset = Check.objects.all()
    serializer_class = CheckSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields = ("status", "type", "printer_id")

    def get(self, request, *args, **kwargs):
        """GET method of the API."""
        return self.list(request, *args, **kwargs)
