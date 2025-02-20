from django import forms
from django.contrib.auth.forms import UserCreationForm
from .models import CustomUser

class RegisterForm(UserCreationForm):
    full_name = forms.CharField(max_length=100)

    class Meta:
        model = CustomUser
        fields = ['username', 'full_name', 'password1', 'password2']
