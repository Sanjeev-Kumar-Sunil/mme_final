# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2018-03-29 05:18
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ContactUs',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sender', models.EmailField(max_length=254)),
                ('subject', models.CharField(max_length=20)),
                ('message', models.CharField(max_length=150)),
                ('cc_myself', models.BooleanField()),
            ],
        ),
    ]
