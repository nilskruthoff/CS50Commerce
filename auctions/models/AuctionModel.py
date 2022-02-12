from django.db import models
from .UserModel import User
from .enums import CategoryChoice


class AuctionModel(models.Model):
    title = models.CharField(max_length=255, default=None)
    description = models.TextField(default=None)
    price = models.DecimalField(decimal_places=2, max_digits=10, default=None)
    category = models.CharField(max_length=255, choices=CategoryChoice.CATEGORY_CHOICES, default=CategoryChoice.MISC)
    created_at = models.DateTimeField(default=None)
    start = models.DateTimeField(default=None)
    end = models.DateTimeField(default=None)
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=None)
    img = models.BinaryField(default=None)
