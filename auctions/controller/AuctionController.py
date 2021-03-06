from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from auctions.forms.AuctionForm import AuctionForm
from auctions.forms.CommentForm import CommentForm
from auctions.models import Auction
from auctions.services import AuctionsService, UserService, WatchlistService, CommentService, BidService


@login_required
def add(request):
    if request.method == 'POST':
        form = AuctionForm(request.POST)
        auction = Auction()
        if form.is_valid():
            return redirect('show_auction', auction.id) \
                if AuctionsService.add_auction(request, auction=auction, form=form) \
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
    bids = BidService.get_all_bids(auction)
    comments = CommentService.get_all_comments(auction)
    auction.update_views()

    return render(request, 'auctions/show.html', {
        "header": auction.title,
        "auction": AuctionsService.prepare_auction(auction, short_description=False),
        "comments": comments,
        "comment_form": CommentForm(),
        "bids": bids,
        "user": auction.user,
        "authenticated": request.user.is_authenticated,
        "on_watchlist": WatchlistService.on_watchlist(auction),
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
