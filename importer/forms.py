from django import forms


class ImporterForm(forms.Form):
    csv_file = forms.FileField()
