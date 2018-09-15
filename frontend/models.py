from django.db import models
from django.utils import timezone
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
