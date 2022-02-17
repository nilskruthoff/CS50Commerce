from django import forms
from django.forms import ModelForm

from auctions.models import Auction
from datetime import datetime, timedelta


class DateInput(forms.DateInput):
    input_type = 'date'


class AuctionForm(ModelForm):
    class Meta:
        model = Auction

        fields = ['title', 'description', 'price', 'category', 'start', 'end', 'shipping', 'img']

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control my-1', 'placeholder': 'Vintage T-Shirt'}),
            'description': forms.Textarea(attrs={'class': 'form-control my-1'}),
            'price': forms.NumberInput(attrs={'class': 'form-control my-1', 'placeholder': '20.00'}),
            'category': forms.Select(attrs={'class': 'form-control my-1'}),
            'start': DateInput(attrs={'class': 'form-control my-1'}),
            'end': DateInput(attrs={'class': 'form-control my-1'}),
            'shipping': forms.Select(attrs={'class': 'form-control my-1'}),
            'img': forms.FileInput(attrs={'class': 'form-control my-1'})
        }
