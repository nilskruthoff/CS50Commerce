from auctions.models import Auction


def get_comments(auction: Auction) -> list:
    return auction.comment_set.all()
