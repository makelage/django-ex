from django.forms import forms,ModelForm
from django.forms.widgets import TimeInput
from . import models


class SignInfoForm(ModelForm):
    class Meta:
        model = models.SignInfo
        fields = ['name', 'date', 'item', 'number']
        widgets = {
            'date': TimeInput(attrs={'class': 'datepicker'}),
        }

