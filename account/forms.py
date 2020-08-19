from django import forms
from django.contrib.auth.forms import UserCreationForm

from account.models import User


class ClientRegisterForm(UserCreationForm):
    phone = forms.CharField(required=True, widget=forms.NumberInput, help_text="Don't include 0, example 7xxxxxxxx")
    password1 = forms.CharField(widget=forms.PasswordInput, help_text='At least 8 characters.', label='Password')
    password2 = forms.CharField(widget=forms.PasswordInput, help_text='Confirm password.', label='Confirm password')

    class Meta:
        model = User
        fields = ('username', 'phone', 'password1', 'password2')


