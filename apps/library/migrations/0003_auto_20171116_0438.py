# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-11-16 04:38
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0002_auto_20171116_0431'),
    ]

    operations = [
        migrations.AddField(
            model_name='author',
            name='notes',
            field=models.TextField(default='No notes for now'),
        ),
        migrations.AddField(
            model_name='book',
            name='desc',
            field=models.TextField(default='No description'),
        ),
    ]
