from django import forms
from django.forms import ModelForm

from auctions.models.User import User


class DateInput(forms.DateInput):
    input_type = 'date'


class UserForm(ModelForm):
    class Meta:
        model = User
        fields = ['prefix', 'first_name', 'last_name', 'gender', 'age', 'birthday', 'street', 'house_number',
                  'postcode', 'city', 'username', 'email', 'password', 'telephone']

        widgets = {
            'prefix': forms.Select(attrs={'class': 'form-control my-2'}),
            'first_name': forms.TextInput(attrs={'class': 'form-control my-2', 'placeholder': 'Firstname'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control my-2', 'placeholder': 'Lastname'}),
            'gender': forms.Select(attrs={'class': 'form-control my-2'}),
            'age': forms.NumberInput(attrs={'class': 'form-control my-2', 'placeholder': 'Age'}),
            'birthday': DateInput(attrs={'class': 'form-control my-2'}),
            'street': forms.TextInput(attrs={'class': 'form-control my-2', 'placeholder': 'Street'}),
            'house_number': forms.TextInput(attrs={'class': 'form-control my-2', 'placeholder': 'House Number'}),
            'postcode': forms.TextInput(attrs={'class': 'form-control my-2', 'placeholder': 'Postcode'}),
            'city': forms.TextInput(attrs={'class': 'form-control my-2', 'placeholder': 'City'}),
            'username': forms.TextInput(attrs={'class': 'form-control my-2', 'placeholder': 'Username'}),
            'email': forms.EmailInput(attrs={'class': 'form-control my-2', 'placeholder': 'Email'}),
            'password': forms.PasswordInput(attrs={'class': 'form-control my-2', 'placeholder': 'Password'}),
            'telephone': forms.TextInput(attrs={'class': 'form-control my-2', 'placeholder': 'Telephone'}),
        }

