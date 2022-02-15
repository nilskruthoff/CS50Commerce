from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _
from django.db import models


class User(AbstractUser):
    class Prefix(models.TextChoices):
        DR = 1, _('Dr.')
        PROF = 2, _('Prof.')
        PROFDR = 3, _('Prof. Dr.')
        PD = 4, _('Priv. Doz.')
        BA = 5, _('B. A.')
        BSC = 6, _('M. A.')
        MA = 7, _('B. Sc')
        MSC = 8, _('M. Sc')


    class Gender(models.TextChoices):
        MALE = 1, _('Male')
        FEMALE = 2, _('Female')
        DIVERSE = 3, _('Diverse')
        NONE = 4, _('No Specification')

    age = models.IntegerField(default=None, blank=True, null=True)
    birthday = models.DateField(default=None, blank=True, null=True)
    postcode = models.CharField(max_length=5, default=None, blank=True, null=True)
    prefix = models.CharField(max_length=2, choices=Prefix.choices, default=None, null=True, blank=True)
    city = models.CharField(max_length=255, default=None, blank=True, null=True)
    street = models.CharField(max_length=255, default=None, blank=True, null=True)
    house_number = models.CharField(max_length=10, default=None, blank=True, null=True)
    telephone = models.CharField(max_length=20, default=None, blank=True, null=True)
    gender = models.CharField(max_length=2, choices=Gender.choices, default=Gender.NONE, null=True, blank=True)