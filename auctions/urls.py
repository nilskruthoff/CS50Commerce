from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register"),
    path("todo/<str:title>", views.todo, name="todo"),
    path("create", views.create_listing, name="create"),
    path("auction/<str:auctions_type>/show", views.render_listings, name="render_auctions"),
    path("auction/<int:auction_id>/", views.listing, name="listing"),
    path("auction/<int:auction_id>/comment", views.add_comment, name="add_comment"),
    path("auction/<int:auction_id>/watchlist/add", views.add_watchlist, name="add_watchlist"),
    path("auction/<int:auction_id>/watchlist/remove", views.remove_watchlist, name="remove_watchlist"),
    path("auction/<int:auction_id>/bid", views.place_bid, name="place_bid")
]
