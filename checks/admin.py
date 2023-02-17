from django.contrib import admin
from checks.models import Check


@admin.register(Check)
class CheckAdmin(admin.ModelAdmin):
    """This class registers Check model at admin site."""

    list_display = (
        "id",
        "printer_id", 
        "type",
        "status", 
        "pdf_file", 
    )
    list_filter = (
        "printer_id",
        "type",
        "status",
    )
    search_fields = (
        "printer_id",
    )

