from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    pass

# class listing(models.Model):
#     title = models.CharField(max_length=20)
#     dec = models.CharField(max_length=64)
#     starting_bid = models.IntegerField()
#     product_image = models.ImageField