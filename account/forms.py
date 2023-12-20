from django import forms
from .models import Customer
# from django.contrib.auth.forms import UserCreationForm, AuthenticationForm



class LoginForm(forms.Form):
    username = forms.CharField(
        max_length=100, widget=forms.TextInput(attrs={
            "placeholder": "Enter Your Username",
            "class": "input-text input-text--primary-style"
        })
    )
    password = forms.CharField(
        max_length=50, widget=forms.PasswordInput(attrs={
            "placeholder": "Enter Your Password",
            "class": "input-text input-text--primary-style"
        })
    )

class CustomerRegistration(forms.ModelForm):
    class Meta:
        model = Customer
        fields = ["first_name", "last_name", "phone_number", "gender", "username", "email", "password"]
        widgets = {
            "first_name": forms.TextInput(attrs={
                    "class": "input-text input-text--primary-style",
                    "placeholder": "Enter First Name",
                }),
            "last_name": forms.TextInput(attrs={
                    "placeholder": "Enter Last Name",
                    "class": "input-text input-text--primary-style"
                }),
            "phone_number": forms.TextInput(attrs={
                    "placeholder": "Enter Phone Number",
                    "class": "input-text input-text--primary-style"
                }),
            "gender": forms.Select(attrs={
                    "placeholder": "Select Gender",
                    "class": "select-box select-box--primary-style u-w-100"
                }),
            "username": forms.TextInput(attrs={
                    "placeholder": "Enter Username",
                    "class": "input-text input-text--primary-style"
                }),
            "email": forms.EmailInput(attrs={
                    "placeholder": "Enter Email Address",
                    "class": "input-text input-text--primary-style"
                }),
            "password": forms.PasswordInput(attrs={
                    "placeholder": "Enter Password",
                    "class": "input-text input-text--primary-style"
                }),
        }

