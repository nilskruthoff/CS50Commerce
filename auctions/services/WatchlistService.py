from auctions.models import Auction
from auctions.models.Watchlist import Watchlist


def on_watchlist(request, auction: Auction):
    return Watchlist.objects.filter(auction_id=auction.id).exists()
