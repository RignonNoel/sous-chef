# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2016-08-26 00:07
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('meal', '0006_auto_20160826_0007'),
        ('member', '0013_auto_20160820_2322'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='clientscheduledstatus',
            options={'ordering': ['change_date']},
        ),
        migrations.AddField(
            model_name='client',
            name='components_to_avoid',
            field=models.ManyToManyField(through='member.Client_avoid_component', to='meal.Component'),
        ),
        migrations.AddField(
            model_name='client',
            name='ingredients_to_avoid',
            field=models.ManyToManyField(through='member.Client_avoid_ingredient', to='meal.Ingredient'),
        ),
        migrations.AddField(
            model_name='client',
            name='options',
            field=models.ManyToManyField(through='member.Client_option', to='member.Option'),
        ),
        migrations.AddField(
            model_name='client',
            name='restrictions',
            field=models.ManyToManyField(through='member.Restriction', to='meal.Restricted_item'),
        ),
        migrations.AlterField(
            model_name='clientscheduledstatus',
            name='client',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='scheduled_statuses', to='member.Client'),
        ),
    ]
