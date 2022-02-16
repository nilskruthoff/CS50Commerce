from datetime import datetime

from auctions.models import Auction, Bid
from auctions.services import AuctionsService


def add_bid(request, bid: Bid, auction: Auction):
    try:
        bid.price = request.POST['price']
        bid.user = request.user
        bid.auction = auction
        auction.price = bid.price
        bid.save()
        auction.save()
        return True
    except ValueError:
        return False


def get_all_bids(auction: Auction):
    bids = auction.bid_set.all()
    for bid in bids:
        bid.date = get_date_time(bid.date)
    return bids


def validate_price(bid, auction):
    return True if float(bid.price) >= float(auction.price) + 1.0 else False


def validate_user(bid: Bid):
    last_bid = bid.auction.get_last_bid()
    return True if last_bid.user != bid.user else False


def get_date_time(date: datetime):
    return date.strftime('%d.%m.%Y %H:%M')