from django.db import models
from django.utils.translation import gettext_lazy as _


class CheckChoice(models.TextChoices):
    KITCHEN = "kitchen", _("Kitchen")
    CLIENT = "client", _("Client")


class Printer(models.Model):
    """
    This class represents the Printer model, which is used to create new printers, store information about them, and manage them.

    Attributes
    ----------
    name : str
        printer name
    api_key : str
        API access key
    check_type : str
        the type of receipt printed by the printer
    point_id : int
        the point to which the printer is bound
    """
    name = models.CharField(
        verbose_name=_("Name"), 
        max_length=128
    )
    api_key = models.CharField(
        verbose_name=_("API key"),
        max_length=128,
        unique=True
    )
    check_type = models.CharField(
        verbose_name=_("Check type"),
        choices=CheckChoice.choices,
        max_length=7
    )
    point_id = models.IntegerField(
        verbose_name=_("Point ID")
    )

    class Meta:
        ordering = ("name",)

    def __str__(self) -> str:
        """Return Printer name"""
        return self.name


    def __repr__(self) -> str:
        """Return Printer name and id"""
        return f"Printer <{self.name}, id:{self.id}>"
