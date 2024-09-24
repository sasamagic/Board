from .models import reg
from django.forms import ModelForm, TextInput
from django import forms


class regForm(ModelForm):
    class Meta:
        model = reg
        fields = ["family", "type", "module_count", "production_date", "history"]
        widgets = {
            "family": forms.Select(attrs={
                'id': 'firstSelect',
                'onchange': 'updateSecondSelect()',
            }),
            "type": forms.Select(attrs={
                'id': 'secondSelect',
            }),
            "module_count": forms.NumberInput(attrs={
                'id': 'modules',
                'min': '1',
                'required': 'required',
            }),
            "production_date": forms.DateInput(attrs={
                'id': 'production-date',
                'required': 'required',
                'type': 'date',
            }),
            "history": forms.Textarea(attrs={
                'id': 'history',
                'maxlength': '10000',
            }),
        }

# форма для ввода серийного номера
