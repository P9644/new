from django import forms
from clientapp.models import Client,User

class ClientForm(forms.ModelForm):
    class Meta:
        model=Client
        fields="__all__"

class UserForm(forms.ModelForm):
    class Meta:
        model=User
        fields="__all__"