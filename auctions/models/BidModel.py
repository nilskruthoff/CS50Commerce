from django.db import models
from .AuctionModel import AuctionModel


class BidModel(models.Model):
    price = models.DecimalField(decimal_places=2, max_digits=10, default=None)
    auction = models.ForeignKey(AuctionModel, on_delete=models.CASCADE, default=None)
