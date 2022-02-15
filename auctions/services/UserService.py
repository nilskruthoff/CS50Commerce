from auctions.models import Auction


def is_owner(request, auction: Auction):
    return auction.user == request.user


def is_authenticated(request):
    return request.user.is_authenticated
