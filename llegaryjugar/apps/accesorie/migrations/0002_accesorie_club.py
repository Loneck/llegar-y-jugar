# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-07-04 17:07
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('clubs', '0001_initial'),
        ('accesorie', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='accesorie',
            name='club',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='accesorie', to='clubs.Club', verbose_name='club'),
        ),
    ]
