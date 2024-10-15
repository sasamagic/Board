from .models import reg
from django.forms import ModelForm
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from .models import info_modules  # Correct import from your app's models
from .models import SPP
# форма для регистрации польхзователя
class info_modulesForm(ModelForm):
    class Meta:
        model = info_modules
        fields = ["info_ec_number", "info_product_family", "info_product_family_code",
                  "info_revision", "info_revision_code", "info_product_type",
                  "info_product_type_code", "info_manufacturer", "info_manufacturer_code"]
        widgets = {
            "info_ec_number": forms.Textarea(attrs={
                'id': 'info-ec-number',  # ID для автозаполнения
                'required': 'required',
                'maxlength': '10000',
            }),
            "info_product_family": forms.Textarea(attrs={
                'id': 'info-product-family',
                'min': '1',
                'required': 'required',
            }),
            "info_product_family_code": forms.NumberInput(attrs={
                'id': 'info-product-family-code',
                'required': 'required',
            }),
            "info_revision": forms.NumberInput(attrs={
                'id': 'info-revision',
                'maxlength': '10000',
                'required': 'required',
            }),
            "info_revision_code": forms.NumberInput(attrs={
                'id': 'info-revision-code',  # ID для автозаполнения
                'required': 'required',
            }),
            "info_product_type": forms.Textarea(attrs={
                'id': 'info-product-type',
                'min': '1',
                'required': 'required',
            }),
            "info_product_type_code": forms.NumberInput(attrs={
                'id': 'info-product-type-code',
                'required': 'required',
            }),
            "info_manufacturer": forms.Textarea(attrs={
                'id': 'info-manufacturer',
                'required': 'required',
                'maxlength': '10000',
            }),
            "info_manufacturer_code": forms.NumberInput(attrs={
                'id': 'info-manufacturer-code',
                'min': '1',
                'required': 'required',
            }),
        }
class regForm(ModelForm):
    class Meta:
        model = reg
        fields = ["ec_number", "module_count", "production_date", "history", "number_of_module"]
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
            "number_of_module": forms.NumberInput(attrs={
                'id': 'number-of-module',
                'min': '1',
                'required': 'required',
            }),
        }

class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


# Форма для стенда СПП
class SPPForm(UserCreationForm):
    class Meta:
        model = SPP
        fields = ["id", "created_at", "user_id", "data", "file"]
        widgets = {
            "id": forms.Textarea(attrs={
                'id': 'SPP-id',
                'min': '1',
            }),
            "created_at": forms.Textarea(attrs={
                'id': 'SPP-created-at',
                'type': 'date',
            }),
            "user_id": forms.NumberInput(attrs={
                'id': 'SPP-user-id',
                'min': '1',
            }),
            "data": forms.NumberInput(attrs={
                'id': 'SPP-data',
                'maxlength': '1000000',
            }),
            "file": forms.NumberInput(attrs={
                'id': 'SPP-file',
            }),
        }
