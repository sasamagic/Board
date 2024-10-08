from .models import reg
from django.forms import ModelForm
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import info_modules  # Correct import from your app's models

# форма для регистрации польхзователя
class regForm(ModelForm):
    class Meta:
        model = reg
        fields = ["ec_number", "module_count", "production_date", "history"]
        widgets = {
            "ec_number": forms.TextInput(attrs={
                'id': 'ec-number',  # ID для автозаполнения
                'class': 'masked',  # Класс для маски
                'required': 'required',
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

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class info_modulesForm(UserCreationForm):
    class Meta:
        model = info_modules
        fields = ["info_ec_number", "info_product_family", "info_revision",
                  "info_product_type", "info_manufacturer", "info_manufacturer_code",
                  "info_product_type_code", "info_revision_code"]
