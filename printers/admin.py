from django.contrib import admin
from printers.models import Printer


@admin.register(Printer)
class PrinterAdmin(admin.ModelAdmin):
    """This class registers Printer model at admin site."""

    list_display = (
        "name", 
        "api_key",
        "check_type", 
        "point_id", 
    )
    list_filter = (
        "check_type",
        "point_id",
    )
    search_fields = (
        "name",
    )

