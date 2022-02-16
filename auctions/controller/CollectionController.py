from django.contrib.auth.decorators import login_required
from django.shortcuts import render

from auctions.models import Auction
from auctions.services import AuctionsService


def show_all(request):
    auctions = AuctionsService.get_all_auctions(length=250)
    return render(request, 'auctions/show_collection.html', {
        'auctions': auctions,
        'header': 'All Auctions'
    })


def show_active(request):
    auctions = AuctionsService.get_active_auctions()
    return render(request, 'auctions/show_collection.html', {
        'auctions': auctions,
        'header': 'Active Auctions'
    })


@login_required
def show_watchlist(request):
    auctions = AuctionsService.get_watchlist_auctions(request)
    return render(request, 'auctions/show_collection.html', {
        'auctions': auctions,
        'header': 'Your Watchlist'
    })


@login_required
def show_user(request):
    auctions = AuctionsService.get_user_auctions(request)
    return render(request, 'auctions/show_collection.html', {
        'auctions': auctions,
        'header': 'Your Auctions'
    })


def show_all_categories(request):
    return render(request, 'auctions/category.html', {'categories': dict(zip(Auction.Category.values, Auction.Category.labels))})


def show_categories(request, category):
    categories = dict(zip(Auction.Category.values, Auction.Category.labels))
    auctions = AuctionsService.get_category_auctions(category)
    return render(request, 'auctions/show_collection.html', {
        'auctions': auctions,
        'header': AuctionsService.get_category(category),
        'new_header': True
    })