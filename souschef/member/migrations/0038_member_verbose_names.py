# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2021-03-05 16:05
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('member', '0037_one_address_per_member'),
    ]

    operations = [
        migrations.AlterField(
            model_name='member',
            name='firstname',
            field=models.CharField(max_length=50, verbose_name='First name'),
        ),
        migrations.AlterField(
            model_name='member',
            name='lastname',
            field=models.CharField(max_length=50, verbose_name='Last name'),
        ),
    ]
