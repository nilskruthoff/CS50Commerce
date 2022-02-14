from django.forms import model_to_dict

from ..models import AuctionModel, User
#TODO Comments
from ..models.WatchlistModel import WatchlistModel


def prepare_auctions(raw_auctions):
    auctions = []
    for auction in raw_auctions:
        auction = model_to_dict(auction)
        auction['url'] = auction['img'].url[16:]
        auction['description'] = auction['description'][:100] + "... (see more)"
        auction['category'] = get_category(auction['category'])
        auctions.append(auction)
    return auctions


def get_all_auctions():
    return prepare_auctions(AuctionModel.objects.all())


def get_active_auctions():
    return prepare_auctions(AuctionModel.objects.filter(is_active=True))


def get_watchlist_auctions(request):
    watchlists = User.objects.get(id=request.user.id).watchlistmodel_set.all()
    auctions = []
    for watchlist in watchlists:
        auctions.append(AuctionModel.objects.get(id=watchlist.auction_id))
    return prepare_auctions(auctions)


def get_user_auctions(request):
    return prepare_auctions(User.objects.get(id=request.user.id).auctionmodel_set.all())


def get_category_auctions(category):
    return prepare_auctions(AuctionModel.objects.filter(category=category))


def get_category(cat):
    return dict(zip(AuctionModel.Category.values, AuctionModel.Category.labels))[cat]


def get_shipping_method(ship):
    return dict(zip(AuctionModel.Shipping.values, AuctionModel.Shipping.labels))[ship]
