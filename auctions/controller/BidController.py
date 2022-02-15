from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect

from auctions.models import Bid, Auction
from auctions.services import AuctionsService, BidService


@login_required
def place_bid(request, auction_id):
    if request.method == 'POST':
        bid = Bid()
        auction = AuctionsService.get_auction(id=auction_id)
        BidService.add_bid(request, bid=bid, auction=auction)
        return redirect('show_auction', auction_id)
    else:
        return redirect('show_auction', auction_id)