from django.contrib import messages
from django.contrib.auth import login, logout, authenticate, get_user_model
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.shortcuts import render, redirect

from auctions.forms.UserForm import UserRegistrationForm


def login_view(request):
    if request.method == "POST":

        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            return redirect('index')
        else:
            return render(request, "auctions/forms/login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "auctions/forms/login.html")


def logout_view(request):
    logout(request)
    return redirect('index')


def register(request):
    if request.method == 'POST':
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f"User created.")
            return redirect('index')
    else:
        form = UserRegistrationForm()
    return render(request, 'auctions/forms/register.html', {'form': form})