from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from auctions.forms.AuctionForm import AuctionForm
from auctions.models import Auction
from auctions.services import AuctionsService, UserService, WatchlistService, CommentService


@login_required
def add(request):
    if request.method == 'POST':
        form = AuctionForm(request.POST)
        if form.is_valid():
            auction = Auction()
            return redirect('show_auction', auction.id) if auction.add_auction(form=form, request=request) \
                else redirect('add_auction')
        else:
            return redirect('add_auction')
    else:
        return render(request, 'auctions/forms/add_auction.html', {
            'page_title': 'Add Auction',
            'header': 'Add a new Auction',
            'form': AuctionForm()
        })


def show(request, auction_id):
    auction = AuctionsService.get_auction(auction_id)

    return render(request, 'auctions/show.html', {
        "header": auction.title,
        "auction": AuctionsService.prepare_auction(auction),
        "comments": CommentService.get_comments(auction),
        "bids": auction.bid_set.all(),
        "user": auction.user,
        "authenticated": request.user.is_authenticated,
        "on_watchlist": WatchlistService.on_watchlist(request, auction),
        "owner": UserService.is_owner(request, auction),
        "has_bids": auction.has_bids(),
        "winner": AuctionsService.has_won(request, auction)
    })


@login_required
def close(request, auction_id):
    auction = AuctionsService.get_auction(auction_id)

    last_bid = auction.get_last_bid()
    auction.is_active = False
    auction.winner = last_bid.user
    auction.save()
    return redirect('index')
