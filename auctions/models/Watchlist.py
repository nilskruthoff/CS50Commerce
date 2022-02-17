from django.db import models

from .Auction import Auction
from .User import User


class Watchlist(models.Model):
    id = models.AutoField(primary_key=True)
    auction = models.ForeignKey(Auction, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
