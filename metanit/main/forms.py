from .models import reg
from django.forms import ModelForm
from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

# class regForm(ModelForm):
#     class Meta:
#         model = reg
#         fields = ["family", "type", "module_count", "production_date", "history"]
#         widgets = {
#             "family": forms.Select(attrs={ # Старая версия регистрации модуля
#                 'id': 'firstSelect',
#                 'onchange': 'updateSecondSelect()',
#             }),
#             "type": forms.Select(attrs={
#                 'id': 'secondSelect',
#             }),
#             "ec_number": forms.Select(attrs={
#                 'id': 'firstSelect',
#             }),
#             "module_count": forms.NumberInput(attrs={
#                 'id': 'modules',
#                 'min': '1',
#                 'required': 'required',
#             }),
#             "production_date": forms.DateInput(attrs={
#                 'id': 'production-date',
#                 'required': 'required',
#                 'type': 'date',
#             }),
#             "history": forms.Textarea(attrs={
#                 'id': 'history',
#                 'maxlength': '10000',
#             }),
#         }

# форма для регистрации польхзователя
class regForm(ModelForm):
    class Meta:
        model = reg
        fields = ["ec_number", "module_count", "production_date", "history"]  # Убираем family и type
        widgets = {
            "ec_number": forms.TextInput(attrs={
                'id': 'ec-number',  # ID для автозаполнения
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


# Для отправки сброса пароля на почту
# class UserForgotPasswordForm(PasswordResetForm):
#     """
#     Запрос на восстановление пароля
#     """
#
#     def __init__(self, *args, **kwargs):
#         """
#         Обновление стилей формы
#         """
#         super().__init__(*args, **kwargs)
#         for field in self.fields:
#             self.fields[field].widget.attrs.update({
#                 'class': 'form-control',
#                 'autocomplete': 'off'
#             })
#
#
# class UserSetNewPasswordForm(SetPasswordForm):
#     """
#     Изменение пароля пользователя после подтверждения
#     """
#
#     def __init__(self, *args, **kwargs):
#         """
#         Обновление стилей формы
#         """
#         super().__init__(*args, **kwargs)
#         for field in self.fields:
#             self.fields[field].widget.attrs.update({
#                 'class': 'form-control',
#                 'autocomplete': 'off'
#             })