# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2018-03-31 13:26
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('expert', '0008_feedback_rating'),
    ]

    operations = [
        migrations.AlterField(
            model_name='feedback',
            name='rating',
            field=models.IntegerField(choices=[(1, 1), (2, 2), (3, 3), (4, 4), (5, 5)]),
        ),
        migrations.AlterField(
            model_name='feedback',
            name='user',
            field=models.CharField(default='anonymous', max_length=30),
        ),
    ]
