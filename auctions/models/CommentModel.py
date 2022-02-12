from django.db import models
from .AuctionModel import AuctionModel


class CommentModel(models.Model):
    comment = models.TextField(default=None)
    auction = models.ForeignKey(AuctionModel, on_delete=models.CASCADE, default=None)

