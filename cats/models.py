"""Cats app models"""

from django.contrib.auth.models import User
from django.db import models


class Cat(models.Model):
    """Cat model"""
    name = models.CharField(max_length=30)
    breed = models.CharField(max_length=20)
    age = models.IntegerField()
    birthday = models.DateField()
    owner = models.ForeignKey(
        to=User,
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return self.name
