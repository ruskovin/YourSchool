from django import forms
from .models import User as Userform
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User


class CustomAuthenticationForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Username', 'autofocus':True}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder':'Password'}))

class django_user_form(forms.ModelForm):
    class Meta:
        model = Userform
        fields = '__all__'
        widgets = {
            'password': forms.TextInput(attrs={'type':'password'})
        }
        