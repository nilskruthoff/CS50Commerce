from django.db import models

from .AuctionModel import AuctionModel
from .UserModel import User


class CommentModel(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=255, default=None)
    comment = models.TextField(default=None)
    date = models.DateTimeField(auto_now_add=True, null=True)
    auction = models.ForeignKey(AuctionModel, on_delete=models.CASCADE, default=None)
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=None)

