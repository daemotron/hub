from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


class UserStat(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    first_flight = models.DateTimeField(default=timezone.now)
    total_flights = models.BigIntegerField(default=0)
    total_hours = models.IntegerField(default=0)
    last_update = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "{} fse statistics".format(self.user.username)
