from rest_framework import serializers
from printers.models import Printer

class PrinterSerializer(serializers.ModelSerializer):
    """This is a serializer class for the Printer model."""
    class Meta:
        model= Printer
        fields = (
            "name",
            "api_key",
            "check_type",
            "point_id"
        )
        