# coding=utf-8
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Subscribe


class SubscribeForm(forms.ModelForm):

    class Meta:
        model = Subscribe
        fields = ['email']
    # def clean_email(self):
    #     email = self.cleaned_data.get('email')
    #     email_base, provider = email.split('@')
    #     domain, ext = provider.split('.')
    #     if not ext == 'edu':
    #         raise forms.ValidationError("Please Enter a valid edu address")
    #     return email


class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True)
    first_name = forms.CharField(max_length=30, required=True)
    last_name = forms.CharField(max_length=30, required=True)

    class Meta:
        model = User
        fields = ("username", "first_name", "last_name", "email", "password1", "password2")

    def save(self, commit=True):
        user = super().save(commit=False)
        user.email = self.cleaned_data["email"]
        user.first_name = self.cleaned_data["first_name"]
        user.last_name = self.cleaned_data["last_name"]
        if commit:
            user.save()
        return user


class LoginForm(forms.Form):
    username = forms.CharField(max_length=150)
    password = forms.CharField(widget=forms.PasswordInput)

