from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect

from auctions.models import Bid, Auction


@login_required
def place_bid(request, auction_id):
    if request.method == 'POST':
        bid = Bid()
        # TODO Validate BIDS
        auction = Auction.objects.get(id=auction_id)
        bid.price = request.POST['price']
        bid.user = request.user
        bid.auction = auction
        bid.save()
        # TODO Message success
        auction.price = bid.price
        auction.save()
        return redirect('show_auction', auction_id=auction_id)
    else:
        # TODO Message fail
        return redirect('show_active', auction_id=auction_id)