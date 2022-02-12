from django.forms import ModelForm
from auctions.models import AuctionModel


class AuctionForm(ModelForm):
    model = AuctionModel
