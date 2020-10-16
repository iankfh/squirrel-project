from django.forms import ModelForm

from .models import SquirrelSighting


class SightingForm(ModelForm):
    class Meta:
        model = SquirrelSighting
        # All other fields are handled in the background
        fields = [
            'unique_squirrel_id',
            'latitude',
            'longitude',
            'shift',
            'date',
            'age',
        ]

