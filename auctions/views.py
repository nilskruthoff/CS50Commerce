from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse
from .forms.AuctionForm import AuctionForm
from .models import User, AuctionModel
from datetime import datetime


def create_listing(request):
    if request.method == 'POST':
        form = AuctionForm(request.POST)
        if form.is_valid():
            auction = AuctionModel()
            auction.title = form.cleaned_data['title']
            auction.description = form.cleaned_data['description']
            auction.price = form.cleaned_data['price']
            auction.category = form.cleaned_data['category']
            auction.start = form.cleaned_data['start']
            auction.end = form.cleaned_data['end']
            auction.user = request.user

            if len(request.FILES) != 0:
                auction.img = request.FILES['img']

            auction.save()
            return render(request, 'auctions/index.html')
        else:
            return HttpResponse("ERROR")
    else:
        return render(request, 'auctions/create_listing.html', {
            'page_title': 'New Auction',
            'header': 'New Auction',
            'subheader': 'Create a new auction listing',
            'form': AuctionForm()
        })


def template(request):
    return render(request, "auctions/layout.html")


def index(request):
    return render(request, "auctions/index.html")


def login_view(request):
    if request.method == "POST":

        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "auctions/login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "auctions/login.html")


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))


def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]

        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "auctions/register.html", {
                "message": "Passwords must match."
            })

        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError:
            return render(request, "auctions/register.html", {
                "message": "Username already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "auctions/register.html")


def todo(request, title):
    return HttpResponse(f"{title.title()} is not implemented yet!!")