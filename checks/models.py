from email.policy import default
from django.db import models
from django.utils.translation import gettext_lazy as _
from printers.models import Printer, CheckChoice



class CheckStatus(models.TextChoices):
    NEW = "new", _("New")
    RENDERED = "rendered", _("Rendered")
    PRINTED = "Printed", _("Printed")


def generate_file_path(instance, filename):
    file_path = f"pdf/{filename}"
    return file_path


class Check(models.Model):
    """
    This class represents the Check model, which is used to create new check, store information about them, and manage them.

    Attributes
    ----------
    printer_id : int
        Printer ID
    type : str
        the type of check
    order : json
        order data
    pdf_file : filepath
        filepath to check file
    """
    printer_id = models.ForeignKey(
        Printer,
        verbose_name=_("Printer ID"),
        on_delete=models.PROTECT,
        related_name="printer"
    )
    type = models.CharField(
        verbose_name=_("Check type"),
        choices=CheckChoice.choices,
        max_length=7
    )
    order = models.JSONField(
        verbose_name=_("Order data"),
        blank=True,
        null=True
    )
    status = models.CharField(
        verbose_name=_("Check status"),
        choices=CheckStatus.choices,
        max_length=8,
        default=CheckStatus.NEW
    )
    pdf_file = models.FileField(
        verbose_name=_("File location"),
        upload_to=generate_file_path,
    )

    class Meta:
        ordering = ("-id",)

    def __str__(self) -> str:
        """Return Check and Printer ID"""
        return f"Check: {self.id}; Printer{self.printer_id}"

    def __repr__(self) -> str:
        """Return Check ID"""
        return f"Check <id:{self.id}>"
