from django.shortcuts import render
from .services import AuctionsService


def index(request):
    auctions = AuctionsService.get_all_auctions()
    return render(request, 'auctions/index.html', {
        "auctions": auctions
    })


