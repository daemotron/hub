import uuid

from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from markdownx.models import MarkdownxField


class FrontItem(models.Model):
    label = models.CharField(max_length=50, verbose_name='Label', default='')
    order = models.IntegerField(verbose_name='Order', default=0)
    icon = models.CharField(max_length=30, verbose_name='FontAwesome Icon Class')
    colour = models.CharField(max_length=30, verbose_name='Bootstrap Colour Class')
    text = MarkdownxField(verbose_name='Text (MarkDown syntax allowed)')

    def __str__(self):
        return self.label

    class Meta:
        ordering = ['order']


class NewsItem(models.Model):
    label = models.CharField(max_length=50, verbose_name='Label')
    date = models.DateTimeField(verbose_name='Time Stamp', default=timezone.now)
    text = MarkdownxField(verbose_name='Text (MarkDown syntax allowed')
    publish = models.BooleanField(verbose_name='Item is public', default=False)

    def __str__(self):
        return self.label

    class Meta:
        ordering = ['-date']


class ContentSnippet(models.Model):
    cid = models.CharField(max_length=100, verbose_name='Content Identifier')
    text = MarkdownxField(verbose_name='Text (MarkDown syntax allowed')

    def __str__(self):
        return self.cid


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    fseid = models.BigIntegerField(verbose_name='FSEconomy User ID', blank=True)
    key = models.CharField(max_length=20, verbose_name='FSEconomy Access Key', default='', blank=True)
    avatar = models.URLField(verbose_name='Avatar URL', max_length=255, blank=True)
    valid = models.BooleanField(verbose_name='Validated Profile', default=False)
    validated = models.DateTimeField(verbose_name='Validation timestamp', blank=True, null=True)
    token = models.UUIDField(verbose_name='Validation token', default=uuid.uuid4, editable=False, unique=True)
    created = models.DateTimeField(verbose_name='Account created', auto_now_add=True)
    updated = models.DateTimeField(verbose_name='Account updated', auto_now=True)

    def __str__(self):
        return self.user.username
