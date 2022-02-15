from django.db import models
from django.utils.translation import gettext_lazy as _
from ckeditor.fields import RichTextField
from django_resized import ResizedImageField

from .User import User


class Auction(models.Model):
    class Category(models.TextChoices):
        FASH = 1, _('Fashion and Accessoires')
        TECH = 2, _('Technology and Electronics')
        TOY = 3, _('Toys and Board Games')
        HOME = 4, _('Home and Furniture')
        ART = 5, _('Art and Culture')
        FILM = 6, _('Movies and Films')
        GARDEN = 7, _('Garden and Terrace')
        PETS = 8, _('Pets')
        MUSIC = 9, _('Music and Instruments')
        GAME = 10, _('Computer- and Videogames')
        MISC = 11, _('Miscellaneous')

    class Shipping(models.TextChoices):
        SHIP = 1, _("Shipping possible")
        PICK = 2, _("Only Pickup")

    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=255, default=None)
    description = models.TextField(default=None)
    price = models.DecimalField(decimal_places=2, max_digits=10, default=None)
    category = models.CharField(max_length=255, choices=Category.choices, default=Category.MISC)
    start = models.DateField(default=None)
    end = models.DateField(default=None)
    is_active = models.BooleanField(default=True)
    view_count = models.IntegerField(default=0, blank=True, null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=None)
    winner = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True, default=None, related_name='winner')
    img = ResizedImageField(size=[1080, 1080], crop=['middle', 'center'], upload_to='auctions/static/resources/%Y/%m/%d', quality=100, blank=True, null=True)
    shipping = models.CharField(max_length=2, choices=Shipping.choices, default=Shipping.SHIP)

    def get_short_description(self, length: int = 100) -> str:
        return self.description[:length]

    def get_url(self) -> str:
        if self.img:
            return self.img.url[16:]
        else:
            return "resources/placeholder.jpg"

    def get_last_bid(self):
        if self.bid_set.exists():
            return list(self.bid_set.all())[-1]

    def has_bids(self) -> bool:
        return True if self.bid_set.exists() > 0 else False

    def update_views(self):
        self.view_count += 1
        self.save()




