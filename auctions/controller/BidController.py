from django.shortcuts import redirect

from auctions.models import BidModel, AuctionModel


def place_bid(request, auction_id):
    if request.method == 'POST':
        bid = BidModel()
        # TODO Validate BIDS
        auction = AuctionModel.objects.get(id=auction_id)
        bid.price = request.POST['price']
        bid.user = request.user
        bid.auction = auction
        bid.save()
        # TODO Message success
        auction.price = bid.price
        auction.save()
        return redirect('listing', auction_id=auction_id)
    else:
        # TODO Message fail
        return redirect('listing', auction_id=auction_id)