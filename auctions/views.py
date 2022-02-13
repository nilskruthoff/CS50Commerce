from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse
from .forms.AuctionForm import AuctionForm
from .forms.CommentForm import CommentForm
from django.forms.models import model_to_dict
#from .models import User, AuctionModel
from .models.AuctionModel import AuctionModel
from .models.UserModel import User
from .models.CommentModel import CommentModel
from .models.enums import CategoryChoice
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


def index(request):
    data = AuctionModel.objects.all()
    auctions = []

    for auction in data:
        auction = model_to_dict(auction)
        auction['url'] = auction['img'].url[16:]
        auction['description'] = auction['description'][:100] + "... (see more)"
        auctions.append(auction)

    return render(request, "auctions/index.html", {
        "auctions": auctions,
    })


def listing(request, id):
    auction = AuctionModel.objects.get(id=id)
    auction_dict = model_to_dict(auction)
    auction_dict['url'] = auction_dict['img'].url[16:]
    return render(request, 'auctions/listing.html', {
        "comments": auction.commentmodel_set.all(),
        "auction": auction_dict,
        "username": auction.user.username
    })


def add_comment(request, auction_id):
    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = CommentModel()
            comment.title = form.cleaned_data['title']
            comment.comment = form.cleaned_data['comment']
            comment.auction = AuctionModel.objects.get(id=auction_id)
            comment.user = request.user

            comment.save()
            return redirect('listing', id=auction_id)
        else:
            return redirect('index')

    else:
        return render(request, 'auctions/comment.html', {
            'auction': AuctionModel.objects.get(id=auction_id),
            'form': CommentForm()
        })


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