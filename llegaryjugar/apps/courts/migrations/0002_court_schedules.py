# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-05-28 22:46
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('schedules', '0002_schedule_club'),
        ('courts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='court',
            name='schedules',
            field=models.ManyToManyField(null=True, to='schedules.Schedule', verbose_name='schedules'),
        ),
    ]
