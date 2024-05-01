from django import forms
from django.contrib.auth.forms import UserCreationForm

class CustomerRegistrationForm(UserCreationForm):
    ussername = forms.CharField(widget= forms.TextInput(attrs= {'autofocus': 'true', 'class': 'form-control'}))
    email = forms.CharField(widget= forms.EmailInput(attrs= {'class': 'form-control'}))
    password1 = forms.CharField(label = 'Password',widget= forms.PasswordInput(attrs= {'class': 'form-control'}))
    password2 = forms.CharField(label = 'Confirm Password',widget= forms.PasswordInput(attrs= {'class': 'form-control'}))
    