# Generated by Django 2.1.1 on 2018-09-15 08:16

from django.db import migrations, models
import django.utils.timezone
import markdownx.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ContentSnippet',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('cid', models.CharField(max_length=100, verbose_name='Content Identifier')),
                ('text', markdownx.models.MarkdownxField(verbose_name='Text (MarkDown syntax allowed')),
            ],
        ),
        migrations.CreateModel(
            name='FrontItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('label', models.CharField(default='', max_length=50, verbose_name='Label')),
                ('order', models.IntegerField(default=0, verbose_name='Order')),
                ('icon', models.CharField(max_length=30, verbose_name='FontAwesome Icon Class')),
                ('colour', models.CharField(max_length=30, verbose_name='Bootstrap Colour Class')),
                ('text', markdownx.models.MarkdownxField(verbose_name='Text (MarkDown syntax allowed)')),
            ],
            options={
                'ordering': ['order'],
            },
        ),
        migrations.CreateModel(
            name='NewsItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('label', models.CharField(max_length=50, verbose_name='Label')),
                ('date', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Time Stamp')),
                ('text', markdownx.models.MarkdownxField(verbose_name='Text (MarkDown syntax allowed')),
                ('publish', models.BooleanField(default=False, verbose_name='Item is public')),
            ],
            options={
                'ordering': ['-date'],
            },
        ),
    ]
