from django.contrib import admin
from auctions.models.AuctionModel import AuctionModel
from auctions.models.BidModel import BidModel
from auctions.models.CommentModel import CommentModel
from auctions.models.UserModel import User


class AuthorAdmin(admin.ModelAdmin):
    pass


admin.site.register(AuctionModel, AuthorAdmin)
admin.site.register(BidModel, AuthorAdmin)
admin.site.register(CommentModel, AuthorAdmin)
admin.site.register(User, AuthorAdmin)
