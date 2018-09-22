from django.db import models


class Contest(models.Model):
    name = models.CharField(max_length=200, verbose_name='Contest Name')

    def __str__(self):
        return self.name
