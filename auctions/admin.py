from django.contrib.admin import ModelAdmin, register

from auctions.models.Auction import Auction
from auctions.models.Bid import Bid
from auctions.models.Comment import Comment
from auctions.models.User import User
from auctions.models.Watchlist import Watchlist


@register(Auction)
class AuctionAdmin(ModelAdmin):
    list_display = ('id', 'title', 'description', 'price', 'category',
                    'start', 'end', 'shipping', 'img', 'is_active', 'view_count', 'user', 'winner')
    icon_name = 'gavel'

@register(User)
class UserAdmin(ModelAdmin):
    list_display = ('id', 'username', 'email', 'password', 'prefix', 'first_name', 'last_name', 'age',
                    'birthday', 'gender', 'postcode', 'city', 'street', 'house_number', 'telephone')
    icon_name = 'group'


@register(Bid)
class BidAdmin(ModelAdmin):
    list_display = ('id', 'price', 'date', 'auction', 'user')
    icon_name = 'monetization_on'


@register(Comment)
class CommentAdmin(ModelAdmin):
    list_display = ('id', 'title', 'comment', 'date', 'auction', 'user')
    icon_name = 'comment'


@register(Watchlist)
class WatchlistAdmin(ModelAdmin):
    list_display = ('id', 'auction', 'user')
    icon_name = 'remove_red_eye'

