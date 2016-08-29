# coding=utf-8
from django import forms
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

