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
        help_text=_('Date of sighting; Format YYYY-MM-DD'),
    )

    Adult = 'Adult'
    Juvenile = 'Juvenile'
    Unknown = '?'

    AGE_CHOICES = [
        (Adult, 'Adult'),
        (Juvenile, 'Juvenile'),
        (Unknown, '?'),
    ]

    age = models.CharField(
        max_length=8,
        help_text=_('Age description'),
        choices=AGE_CHOICES,
        blank=True,
    )

   # Create your models here.
