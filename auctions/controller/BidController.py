from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import redirect
from django.contrib import messages

from auctions.models import Bid, Auction
from auctions.services import AuctionsService, BidService


@login_required
def place_bid(request, auction_id):
    if request.method == 'POST':
        bid = Bid()
        auction = AuctionsService.get_auction(id=auction_id)
        bid.price = float(request.POST['price'])
        bid.user = request.user
        bid.auction = auction

        is_valid, message = BidService.bid_is_valid(bid, auction)
        if is_valid:
            auction.price = bid.price
            bid.save()
            auction.save()
            messages.success(request, message)
        else:
            messages.error(request, message)

        return redirect('show_auction', auction_id)
    else:
        return redirect('show_auction', auction_id)
