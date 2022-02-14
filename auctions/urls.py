from django.urls import path

from . import views
from .controller import WatchlistController, BidController, \
    CommentController, AuctionController, \
    CollectionController, UserController

urlpatterns = [
    path("", views.index, name="index"),
    path("user/login", UserController.login_view, name="login"),
    path("user/logout", UserController.logout_view, name="logout"),
    path("user/register", UserController.register, name="register"),
    path("auction/add", AuctionController.add, name="add_auction"),
    path("auction/<int:auction_id>/close", AuctionController.close, name="close_auction"),
    path("auction/show/all", CollectionController.show_all, name="show_all"),
    path("auction/show/active", CollectionController.show_active, name="show_active"),
    path("auction/show/watchlist", CollectionController.show_watchlist, name="show_watchlist"),
    path("auction/show/user", CollectionController.show_user, name="show_user"),
    path("category/<str:category>", CollectionController.show_categories, name="show_categories"),
    path("auction/<int:auction_id>/show", AuctionController.show, name="show_auction"),
    path("auction/<int:auction_id>/comment", CommentController.add_comment, name="add_comment"),
    path("auction/<int:auction_id>/watchlist/add", WatchlistController.add_watchlist, name="add_watchlist"),
    path("auction/<int:auction_id>/watchlist/remove", WatchlistController.remove_watchlist, name="remove_watchlist"),
    path("auction/<int:auction_id>/bid", BidController.place_bid, name="place_bid")
]
