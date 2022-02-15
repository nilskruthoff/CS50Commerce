from auctions.models import Auction, Bid
from auctions.services import AuctionsService


def add_bid(request, bid: Bid, auction: Auction):
    try:
        bid.price = request.POST['price']
        bid.user = request.user
        bid.auction = auction
        auction.price = bid.price
        if not validate_price(bid=bid, auction=auction):
            return False
        if not validate_user(bid):
            return False
        bid.save()
        auction.save()
        return True
    except:
        return False


def validate_price(bid, auction):
    return True if bid.price > auction.price + 1.0 else False


def validate_user(bid: Bid):
    last_bid = bid.auction.get_last_bid()
    return True if last_bid.user != bid.user else False



