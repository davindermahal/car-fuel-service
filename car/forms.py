from django.forms import ModelForm, DateTimeInput

from .models import Car


class CarForm(ModelForm):
    class Meta:
        model = Car
        fields = ['name', 'vin', 'license_plate', 'purchase_date', 'sell_date', 'year', 'manufacturer', 'model',
                  'tire_size', 'tire_pressure']
