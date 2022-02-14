from django.forms import model_to_dict
from django.http import HttpResponse
from django.shortcuts import render, redirect

from auctions.forms.AuctionForm import AuctionForm
from auctions.models import AuctionModel
from auctions.models.WatchlistModel import WatchlistModel


def add(request):
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
        return render(request, 'auctions/add_auction.html', {
            'page_title': 'New Auction',
            'header': 'New Auction',
            'subheader': 'Create a new auction listing',
            'form': AuctionForm()
        })


def show(request, auction_id):
    auction = AuctionModel.objects.get(id=auction_id)
    auction_dict = model_to_dict(auction)
    auction_dict['url'] = auction_dict['img'].url[16:]

    is_watchlist = False
    if WatchlistModel.objects.filter(auction_id=auction_id).exists():
        is_watchlist = True

    is_owner = False
    if auction.user == request.user:
        is_owner = True

    has_won = False
    if request.user == auction.winner:
        has_won = True

    return render(request, 'auctions/show.html', {
        "auction": auction_dict,
        "comments": auction.commentmodel_set.all(),
        "bids": auction.bidmodel_set.all(),
        "username": auction.user.username,
        "is_watchlist": is_watchlist,
        "is_owner": is_owner,
        "has_won": has_won
    })


def close(request, auction_id):
    auction = AuctionModel.objects.get(id=auction_id)
    last_bid = list(auction.bidmodel_set.all())[-1]
    auction.is_active = False
    auction.winner = last_bid.user
    auction.save()
    return redirect('index')