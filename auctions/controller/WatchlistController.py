from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import redirect

from auctions.models import Auction
from auctions.models.Watchlist import Watchlist
from auctions.services import AuctionsService, WatchlistService


@login_required
def add_watchlist(request, auction_id):
    watchlist = Watchlist()
    auction = AuctionsService.get_auction(id=auction_id)
    WatchlistService.add_watchlist(request, watchlist=watchlist, auction=auction)
    return redirect('show_auction', auction.id)


@login_required
def remove_watchlist(request, auction_id):
    auction = AuctionsService.get_auction(id=auction_id)
    if WatchlistService.on_watchlist(auction):
        Watchlist.objects.filter(user_id=request.user.id, auction_id=auction_id).delete()
        return redirect('show_auction', auction.id)
    else:
        return redirect('show_auction', auction.id)