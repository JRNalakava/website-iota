from django.db import models
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import AbstractUser
from . import script
from localflavor.us.models import USStateField


# Create your models here.
class User(AbstractUser):
    is_brother = models.BooleanField(default=True)
    is_pledge = models.BooleanField(default=False)

    pledge_class = models.TextField(null=False, default='PC', max_length=5)

    user_city = USStateField()
    user_city = models.TextField(null=True, max_length=50)
    major = models.TextField(null=False, max_length=50, default='Unspecified')
    avatar = models.ImageField(upload_to='images', null=True)


class Member(models.Model):
    user = models.ForeignKey(to=User, on_delete=models.CASCADE)
    paid_dues = models.BooleanField(default=False)
    expected_graduation_date = models.TextField(null=False, default='May 2020')


class Active(models.Model):
    member = models.ForeignKey(to=Member, on_delete=models.CASCADE)
    rush_credits = models.PositiveSmallIntegerField(default=0)
    philanthropy_credits = models.PositiveSmallIntegerField(default=0)
    professional_credits = models.PositiveSmallIntegerField(default=0)
    tech_credits = models.PositiveSmallIntegerField(default=0)


class Alumni(models.Model):
    industry = models.TextField(null=True, max_length=50)
    graduation_date = models.TextField(default='May 2018')
