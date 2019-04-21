from django.contrib.auth import get_user_model
from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    venmo = models.CharField(max_length=255)


class Downtown(models.Model):
    name = models.CharField(max_length=255)
    location = models.CharField(max_length=255)
    time = models.DateTimeField()

    def __str__(self):
        return self.name


class Ticket(models.Model):
    price = models.IntegerField()
    seller = models.ForeignKey(get_user_model(), on_delete=models.DO_NOTHING)
    downtown = models.ForeignKey(Downtown, on_delete=models.DO_NOTHING)

    def __str__(self):
        return str(self.seller) + ': ' + str(self.downtown)
