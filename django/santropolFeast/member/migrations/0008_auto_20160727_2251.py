# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-07-27 22:51
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('member', '0007_auto_20160726_1703'),
    ]

    operations = [
        migrations.RenameField(
            model_name='address',
            old_name='lat',
            new_name='latitude',
        ),
        migrations.RenameField(
            model_name='address',
            old_name='lon',
            new_name='longitude',
        ),
    ]
