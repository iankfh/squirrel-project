from django.forms import ModelForm

from .models import SquirrelSighting


class SightingForm(ModelForm):
    class Meta:
        model = SquirrelSighting
        
        fields = [
            'unique_squirrel_id',
            'latitude',
            'longitude',
            'shift',
            'date',
            'age',
        ]

