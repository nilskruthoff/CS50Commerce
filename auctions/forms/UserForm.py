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
            'prefix': forms.Select(attrs={'class': 'form-control my-1'}),
            'first_name': forms.TextInput(attrs={'class': 'form-control my-1', 'placeholder': 'Jake'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control my-1', 'placeholder': 'Miller'}),
            'gender': forms.Select(attrs={'class': 'form-control my-1'}),
            'age': forms.NumberInput(attrs={'class': 'form-control my-1', 'placeholder': '25'}),
            'birthday': DateInput(attrs={'class': 'form-control my-1', 'value': '01.01.1990'}),
            'street': forms.TextInput(attrs={'class': 'form-control my-1', 'placeholder': 'St. Mark\'s Place'}),
            'house_number': forms.TextInput(attrs={'class': 'form-control my-1', 'placeholder': '1'}),
            'postcode': forms.TextInput(attrs={'class': 'form-control my-1', 'placeholder': '10003'}),
            'city': forms.TextInput(attrs={'class': 'form-control my-1', 'placeholder': 'New York'}),
            'username': forms.TextInput(attrs={'class': 'form-control my-1', 'placeholder': 'jake_miller'}),
            'email': forms.EmailInput(attrs={'class': 'form-control my-1', 'placeholder': 'jake.miller@auctions.com'}),
            'password': forms.PasswordInput(attrs={'class': 'form-control my-1', 'placeholder': 'Password'}),
            'telephone': forms.TextInput(attrs={'class': 'form-control my-1', 'placeholder': '(+49) 1635 02475378'}),
        }

