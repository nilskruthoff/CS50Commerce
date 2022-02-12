from django.forms import ModelForm
from django import forms
from auctions.models import AuctionModel


class DateInput(forms.DateInput):
    input_type = 'date'


class AuctionForm(ModelForm):
    class Meta:
        model = AuctionModel

        fields = ['title', 'description', 'price', 'category', 'start', 'end', 'img']
        label = {
            'title': 'Auction Title',
            'description': 'Product Description',
            'price': 'Initial Bid',
            'category': 'Category',
            'start': 'Auction Start',
            'end': 'Auction End',
            'img': 'Product Picture'
        }
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control my-2', 'placeholder': 'e.g Vintage T-Shirt'}),
            'description': forms.Textarea(attrs={'class': 'form-control my-2'}),
            'price': forms.NumberInput(attrs={'class': 'form-control my-2', 'placeholder': 'e.g 20.00€'}),
            'category': forms.Select(attrs={'class': 'form-control my-2', 'placeholder': 'e. g Technology and Electronics'}),
            'start': DateInput(attrs={'class': 'form-control my-2', 'placeholder': 'MM-DD-YYYY HH:SS'}),
            'end': DateInput(attrs={'class': 'form-control my-2', 'placeholder': 'MM-DD-YYYY HH:SS'}),
            'img': forms.ClearableFileInput(attrs={'class': 'form-control my-2', 'placeholder': 'Upload a picture for your '
                                                                                           'auction'})
        }
