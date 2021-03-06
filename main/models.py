from django.contrib.auth import get_user_model
from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    venmo = models.CharField(max_length=255)
    following = models.ManyToManyField('self', symmetrical=False, blank=True)
    attending = models.ManyToManyField('Downtown', blank=True)


class Downtown(models.Model):
    name = models.CharField(max_length=255)
    location = models.CharField(max_length=255)
    bio = models.TextField(default='')
    time = models.DateTimeField()

    def __str__(self):
        return self.name


class Ticket(models.Model):
    price = models.PositiveIntegerField()
    seller = models.ForeignKey(get_user_model(), on_delete=models.DO_NOTHING)
    downtown = models.ForeignKey(Downtown, on_delete=models.DO_NOTHING)
    bio = models.TextField(default='')
    sold = models.BooleanField(default=False)

    class Meta:
        ordering = ['price']

    def __str__(self):
        return str(self.seller) + ': ' + str(self.downtown)
