from django.forms import model_to_dict

from ..models import Auction, User


def prepare_auction(auction: Auction, short_description: bool = True) -> Auction:
    auction.url = auction.get_url()
    if short_description:
        auction.description = auction.get_short_description()
    auction.category = get_category(auction.category)
    return auction


def prepare_auctions(raw_auctions) -> list:
    auctions = []
    for auction in raw_auctions:
        auction = model_to_dict(auction)
        if auction['img']:
            auction['url'] = auction['img'].url[16:]
        auction['description'] = auction['description'][:100] + "... (see more)"
        auction['category'] = get_category(auction['category'])
        auctions.append(auction)
    return auctions


def get_auction(id: int) -> Auction:
    return Auction.objects.get(id=id)


def get_all_auctions() -> list:
    return prepare_auctions(Auction.objects.all())


def get_active_auctions() -> list:
    return prepare_auctions(Auction.objects.filter(is_active=True))


def get_watchlist_auctions(request) -> list:
    watchlists = User.objects.get(id=request.user.id).watchlist.all()
    auctions = []
    for watchlist in watchlists:
        auctions.append(Auction.objects.get(id=watchlist.auction_id))
    return prepare_auctions(auctions)


def get_user_auctions(request) -> list:
    return prepare_auctions(User.objects.get(id=request.user.id).Auction_set.all())


def get_category_auctions(category: str) -> list:
    return prepare_auctions(Auction.objects.filter(category=category))


def has_won(request, auction: Auction) -> bool:
    return auction.winner == request.user


def get_category(category) -> dict:
    return dict(zip(Auction.Category.values, Auction.Category.labels))[category]


def get_shipping_method(shipping) -> dict:
    return dict(zip(Auction.Shipping.values, Auction.Shipping.labels))[shipping]
