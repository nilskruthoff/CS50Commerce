from auctions.models import Auction
from auctions.models.Watchlist import Watchlist


def on_watchlist(auction: Auction):
    return Watchlist.objects.filter(auction_id=auction.id).exists()


def add_watchlist(request, watchlist: Watchlist, auction: Auction):
    if not on_watchlist(auction):
        try:
            watchlist.user = request.user
            watchlist.auction = auction
            watchlist.save()
            return True
        except ValueError:
            return False
    else:
        return False