from rest_framework import serializers
from checks.models import Check

class CreateCheckSerializer(serializers.ModelSerializer):
    """This is a serializer class for create new Check."""
    class Meta:
        model= Check
        fields = (
            "printer_id",
            "type",
            "order",
        )
        

class CheckSerializer(serializers.ModelSerializer):
    """This is a serializer class for the Check models."""
    class Meta:
        model= Check
        fields = (
            "printer_id",
            "type",
            "order",
            "status",
            "pdf_file"
        )
        