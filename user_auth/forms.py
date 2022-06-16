from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class CreateUserForm(UserCreationForm):
    username = forms.CharField(max_length=256, required=True, widget=forms.TextInput(attrs={
        'class': 'form-control',
    }))

    email = forms.EmailField(widget=forms.EmailInput(attrs={
        'class': 'form-control',
    }))

    password1 = forms.CharField(max_length=256, required=True, widget=forms.PasswordInput(attrs={
        'class': 'form-control',
    }))

    password2 = forms.CharField(max_length=256, required=True, widget=forms.PasswordInput(attrs={
        'class': 'form-control',
    }))

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
