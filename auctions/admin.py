from django.contrib import admin

from auctions.models.Auction import Auction
from auctions.models.Bid import Bid
from auctions.models.Comment import Comment
from auctions.models.User import User
from auctions.models.Watchlist import Watchlist


class AuthorAdmin(admin.ModelAdmin):
    pass


admin.site.register(Auction, AuthorAdmin)
admin.site.register(Bid, AuthorAdmin)
admin.site.register(Comment, AuthorAdmin)
admin.site.register(User, AuthorAdmin)
admin.site.register(Watchlist, AuthorAdmin)
