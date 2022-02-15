from django import forms
from django.forms import ModelForm

from auctions.models import Auction


class DateInput(forms.DateInput):
    input_type = 'date'


class AuctionForm(ModelForm):
    class Meta:
        model = Auction

        fields = ['title', 'description', 'price', 'category', 'start', 'end', 'shipping', 'img']
        label = {
            'title': 'Auction Title',
            'description': 'Product Description',
            'price': 'Initial Bid',
            'category': 'Category',
            'start': 'Auction Start',
            'end': 'Auction End',
            'shipping': 'Shipping Method',
            'img': 'Product Image'
        }
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control my-2', 'placeholder': 'e.g Vintage T-Shirt'}),
            'description': forms.Textarea(attrs={'class': 'form-control my-2'}),
            'price': forms.NumberInput(attrs={'class': 'form-control my-2', 'placeholder': 'e.g 20.00€'}),
            'category': forms.Select(attrs={'class': 'form-control my-2'}),
            'start': DateInput(attrs={'class': 'form-control my-2', 'placeholder': 'MM-DD-YYYY HH:SS'}),
            'end': DateInput(attrs={'class': 'form-control my-2', 'placeholder': 'MM-DD-YYYY HH:SS'}),
            'shipping': forms.Select(attrs={'class': 'form-control my-2'}),
            'img': forms.FileInput(attrs={'class': 'form-control my-2'})
        }
