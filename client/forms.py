from django import forms

from account.models import User
from client.models import BreakDownRequest


class ClientPrimary(forms.ModelForm):
    client_location = forms.CharField(max_length=500, widget=forms.HiddenInput(attrs={'id': 'client_location'}))
    breakdown_description = forms.CharField(widget=forms.Textarea(attrs={'rows': 3, 'col': 15}), required=False)
    #requesting_client = forms.CharField(required=False, widget=forms.HiddenInput(attrs={'id': 'user'}))

    class Meta:
        model = BreakDownRequest
        fields = ('client_location', 'towing', 'flat_tire', 'engine_down', 'vehicle', 'client_zone', 'breakdown_description')


class ClientSecondary(forms.ModelForm):
    breakdown_description = forms.CharField(widget=forms.Textarea(attrs={'rows': 3, 'col': 15}), required=False)

    class Meta:
        model = BreakDownRequest
        fields = ('client_zone', 'breakdown_description')


class UserUpdateForm(forms.ModelForm):

    class Meta:
        model = User
        fields = ('username', 'phone', 'email', 'first_name', 'last_name')
