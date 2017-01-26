from django import forms
from .models import FillUp
from car.models import Car
from fuel.models import Brand, Location


class FillUpForm(forms.ModelForm):
    pass
#
#     def __init__(self, *args, **kwargs):
#         user_id = kwargs['user_id']
#         car_id = kwargs['car_id']
#         del kwargs['user_id']
#         del kwargs['car_id']
#         super(FillUpForm, self).__init__(*args, **kwargs)
#
#         # self.fields['car'].queryset = Car.objects.filter(user_id=user_id)
#         self.fields['car'].queryset = Car.objects.filter(pk=car_id, user_id=user_id)
#         self.fields['fuel_brand'].queryset = Brand.objects.filter(user_id=user_id)
#         self.fields['location'].queryset = Location.objects.filter(user_id=user_id)
#
#     class Meta:
#         model = FillUp
#         fields = ['car', 'date_time', 'odometer', 'filled_up', 'unit_cost_per', 'unit_quantity', 'total_cost', 'octane',
#                   'fuel_brand', 'location']
#
#         widgets = {
#             'date_time': DateTimeInput(format='%Y-%m-%d %H:%M')
#         }
#
#         labels = {
#             'car': 'Vehicle',
#             'unit_cost_per': 'Cost/Gallon',
#             'unit_quantity': 'Gallons',
#             'fuel_brand': 'Gas Brand',
#         }


class CustomFillUpForm(forms.Form):

    odometer = forms.IntegerField(min_value=0, required=False)
    date_time = forms.DateTimeField(input_formats='%Y-%m-%d %H:%M', required=False)  # widget=forms.SelectDateWidget()
    filled_up = forms.ChoiceField(choices=FillUp.FILL_UPS)
    unit_cost_per = forms.FloatField(label="Cost/Gallon", min_value=0, required=False)
    unit_quantity = forms.FloatField(label="Gallons", min_value=0, required=False)
    total_cost = forms.FloatField(min_value=0, required=False)
    octane = forms.ChoiceField(choices=FillUp.OCTANE)
    fuel_brand = forms.ModelChoiceField(queryset=None, required=False)
    location = forms.ModelChoiceField(queryset=None, required=False)
    notes = forms.CharField(widget=forms.Textarea({'rows': 5}), required=False, max_length=255)
    services = forms.CharField(widget=forms.Textarea({'rows': 5}), required=False, max_length=255)

    def __init__(self, *args, **kwargs):

        user_id = kwargs['user_id']
        car_id = kwargs['car_id'] # need for validation
        del kwargs['user_id']
        del kwargs['car_id']
        super(CustomFillUpForm, self).__init__(*args, **kwargs)

        self.fields['fuel_brand'].queryset = Brand.objects.filter(user_id=user_id)
        self.fields['location'].queryset = Location.objects.filter(user_id=user_id)





