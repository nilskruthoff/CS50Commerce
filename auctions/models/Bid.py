from django.db import models

from .Auction import Auction
from .User import User


class Bid(models.Model):
    id = models.AutoField(primary_key=True)
    price = models.DecimalField(decimal_places=2, max_digits=10)
    auction = models.ForeignKey(Auction, on_delete=models.CASCADE)
    date = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

