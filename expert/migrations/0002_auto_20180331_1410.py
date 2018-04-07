# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2018-03-31 08:40
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('expert', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='expert',
            name='department',
            field=models.CharField(choices=[('Agriculture', 'Agriculture'), ('Automotive', 'Automotive'), ('Business', 'Business'), ('Career', 'Career'), ('Education', 'Education'), ('Finance', 'Finance'), ('Fitness', 'Fitness'), ('Health', 'Health'), ('Legal', 'Legal'), ('Lifestyle', 'Lifestyle'), ('RealEstate', 'RealEstate'), ('Spiritual', 'Spiritual'), ('Tax and Accounting', 'Tax and Accounting'), ('Technology', 'Technology'), ('Travels', 'Travels')], default='other', max_length=50),
        ),
        migrations.AddField(
            model_name='expert',
            name='profession',
            field=models.CharField(choices=[('Doctor', 'Doctor'), ('Engineer', 'Engineer'), ('Lawyer', 'Lawyer'), ('MBA', 'MBA'), ('Professor', 'Professor'), ('Businessman', 'Businessman'), ('Athlete', 'Athlete'), ('Actor', 'Actor'), ('Consultant', 'Consultant'), ('Spiritualist', 'Spiritualist'), ('others', 'others')], default='other', max_length=50),
        ),
    ]