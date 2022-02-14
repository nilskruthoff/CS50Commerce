from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import redirect

from auctions.models import AuctionModel
from auctions.models.WatchlistModel import WatchlistModel


@login_required
def add_watchlist(request, auction_id):
    if not WatchlistModel.objects.filter(auction_id=auction_id).exists():
        watch_list = WatchlistModel()
        watch_list.user = request.user
        watch_list.auction = AuctionModel.objects.get(id=auction_id)
        watch_list.save()
        # TODO Message success
        return redirect('listing', auction_id=auction_id)
    else:
        # TODO Message Fail
        return HttpResponse(f"Auction is already in watchlist")


@login_required
def remove_watchlist(request, auction_id):
    if WatchlistModel.objects.filter(auction_id=auction_id).exists():
        WatchlistModel.objects.filter(user_id=request.user.id, auction_id=auction_id).delete()
        # TODO Message success
        return redirect('listing', auction_id=auction_id)
    else:
        # TODO Message Fail
        return HttpResponse(f"Auction is not in watchlist")