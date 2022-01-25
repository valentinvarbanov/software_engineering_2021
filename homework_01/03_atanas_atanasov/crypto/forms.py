from django.forms import ModelForm
from django import forms

from .models import Currency

class CoinForm(ModelForm):
    class Meta:
        model = Currency
        fields = '__all__'