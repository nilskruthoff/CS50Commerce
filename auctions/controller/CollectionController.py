from django.shortcuts import render

from auctions.models import AuctionModel
from auctions.services import AuctionsService


def show_all(request):
    auctions = AuctionsService.get_all_auctions()
    return render(request, 'auctions/index.html', {'auctions': auctions})


def show_active(request):
    auctions = AuctionsService.get_active_auctions()
    return render(request, 'auctions/index.html', {'auctions': auctions})


def show_watchlist(request):
    auctions = AuctionsService.get_watchlist_auctions(request)
    return render(request, 'auctions/index.html', {'auctions': auctions})


def show_user(request):
    auctions = AuctionsService.get_user_auctions(request)
    return render(request, 'auctions/index.html', {'auctions': auctions})


def show_categories(request, category):
    categories = dict(zip(AuctionModel.Category.values, AuctionModel.Category.labels))
    if category == 'all':
        return render(request, 'auctions/category.html', {'categories': categories})
    else:
        auctions = AuctionsService.get_category_auctions(category)
        return render(request, 'auctions/index.html', {'auctions': auctions})