from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import ModelForm

from auctions.models.User import User


class DateInput(forms.DateInput):
    input_type = 'date'


class UserRegistrationForm(UserCreationForm):
    email = forms.EmailField()
    prefix = forms.Select()
    first_name = forms.TextInput()
    last_name = forms.TextInput()
    gender = forms.Select()
    age = forms.NumberInput()
    birthday = DateInput(),
    street = forms.TextInput(),
    house_number = forms.TextInput(),
    postcode = forms.TextInput(),
    city = forms.TextInput(),
    username = forms.TextInput(),
    password = forms.PasswordInput(),

    class Meta:
        model = User
        fields = ['prefix', 'first_name', 'last_name', 'gender', 'age', 'birthday', 'street', 'house_number',
                  'postcode', 'city', 'username', 'email', 'password1', 'password2']


