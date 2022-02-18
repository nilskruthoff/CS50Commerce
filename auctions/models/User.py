from django.contrib.auth.base_user import BaseUserManager
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import gettext_lazy as _


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

    age = models.IntegerField()
    birthday = models.DateField()
    postcode = models.CharField(max_length=5,)
    prefix = models.CharField(max_length=2, choices=Prefix.choices, blank=True, null=True, default=None)
    city = models.CharField(max_length=255)
    street = models.CharField(max_length=255)
    house_number = models.CharField(max_length=10)
    telephone = models.CharField(max_length=20)
    gender = models.CharField(max_length=2, choices=Gender.choices, default=Gender.MALE)


class UserManager(BaseUserManager):
    def create_user(self, email, password=None):
        """
        Creates and saves a User with the given email and password.
        """
        if not email:
            raise ValueError('Users must have an email address')

        user = self.model(
            email=self.normalize_email(email),
        )

        user.set_password(password)
        user.save(using=self._db)
        return user