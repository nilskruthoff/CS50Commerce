from datetime import datetime

from auctions.models import Auction, Bid


def add_bid(request, bid: Bid, auction: Auction):
        bid.price = float(request.POST['price'])
        bid.user = request.user
        bid.auction = auction
        auction.price = bid.price
        bid.save()
        auction.save()
        return True


def get_all_bids(auction: Auction):
    bids = auction.bid_set.all()
    for bid in bids:
        bid.date = get_date_time(bid.date)
    return bids


def bid_is_valid(bid: Bid, auction: Auction):
    if validate_format(bid) and validate_own_auction(bid, auction) and\
            validate_last_bid(bid, auction) and validate_price(bid, auction):
        return True, "Your Bid was successfully placed!"
    else:
        if not validate_format(bid):
            return False, "The Bid must be a Decimal (e. g 30.00) or an Integer (e. g 30)!"
        if not validate_own_auction(bid, auction):
            return False, "You cannot bid on your own Auction!"
        if not validate_last_bid(bid, auction):
            return False, "The last Bid is already your Bid!"
        if not validate_price(bid, auction):
            return False, "The Bid price must be higher than the current Auction price!"
        else:
            return False, "Something went wrong, please place your Bid again!"


def validate_format(bid: Bid):
    if type(bid.price) == float or type(bid.price) == int:
        return True
    else:
        return False


def validate_price(bid, auction):
    if float(bid.price) > float(auction.price):
        return True
    else:
        return False


def validate_own_auction(bid: Bid, auction: Auction):
    if bid.user != auction.user:
        return True
    else:
        return False


def validate_last_bid(bid: Bid, auction: Auction):
    if len(auction.bid_set.all()) > 0:
        last_bid = bid.auction.get_last_bid()
        if last_bid.user != bid.user:
            return True
        else:
            return False
    else:
        return True



def get_date_time(date: datetime):
    return date.strftime('%d.%m.%Y %H:%M')