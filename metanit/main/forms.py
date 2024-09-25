from .models import reg
from django.forms import ModelForm, TextInput
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

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

# форма для регистрации польхзователя

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']