from django.db import models

from .Auction import Auction
from .User import User


class Comment(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=255)
    comment = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    auction = models.ForeignKey(Auction, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

