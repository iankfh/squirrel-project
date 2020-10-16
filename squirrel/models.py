from django.db import models
from django.utils.translation import gettext as _


class SquirrelSighting(models.Model):
    unique_squirrel_id = models.CharField(
        max_length=500,
        help_text=_('Unique Squirrel ID'),
        unique=True,
    )

    latitude = models.FloatField(
        help_text=_('Latitude'),
    )

    longitude = models.FloatField(
        help_text=_('Longitude'),
    )

    AM = 'AM'
    PM = 'PM'

    SHIFT_CHOICES = [
        (AM, 'AM'),
        (PM, 'PM'),
    ]

    shift = models.CharField(
        max_length=2,
        help_text=_('AM or PM'),
        choices=SHIFT_CHOICES,
    )

    date = models.DateField(
        help_text=_('Date of sighting'),
    )

    age = models.CharField(
        max_length=100,
        help_text=_('Age description'),
        blank=True,
    )

   # Create your models here.
