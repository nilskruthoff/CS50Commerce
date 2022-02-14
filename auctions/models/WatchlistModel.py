from django.db import models

from .AuctionModel import AuctionModel
from .UserModel import User


class WatchlistModel(models.Model):
    id = models.AutoField(primary_key=True)
    auction = models.ForeignKey(AuctionModel, on_delete=models.CASCADE, default=None)
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=None)
