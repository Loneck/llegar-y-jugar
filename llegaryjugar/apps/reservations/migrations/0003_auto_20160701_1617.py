# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-07-01 20:17
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('courts', '0005_auto_20160626_1121'),
        ('accesorie', '0001_initial'),
        ('clubs', '0001_initial'),
        ('reservations', '0002_auto_20160701_1353'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='reservations',
            name='res_accesorie',
        ),
        migrations.RemoveField(
            model_name='reservations',
            name='res_club',
        ),
        migrations.RemoveField(
            model_name='reservations',
            name='res_court',
        ),
        migrations.RemoveField(
            model_name='reservations',
            name='res_price',
        ),
        migrations.RemoveField(
            model_name='reservations',
            name='res_schedule',
        ),
        migrations.AddField(
            model_name='reservations',
            name='accesorie',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='accesorie', to='accesorie.Accesorie'),
        ),
        migrations.AddField(
            model_name='reservations',
            name='club',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='club_name', to='clubs.Club'),
        ),
        migrations.AddField(
            model_name='reservations',
            name='price',
            field=models.DecimalField(decimal_places=2, max_digits=30, null=True, verbose_name='price'),
        ),
        migrations.AddField(
            model_name='reservations',
            name='schedule',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='schedule_schedule', to='courts.ScheduleCourt', verbose_name='scheduleCourt'),
        ),
    ]
