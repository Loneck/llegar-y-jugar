# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-07-04 17:07
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('reservations', '0003_auto_20160701_1617'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reservations',
            name='schedule',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='schedule_schedule', to='courts.ScheduleCourt'),
        ),
    ]
