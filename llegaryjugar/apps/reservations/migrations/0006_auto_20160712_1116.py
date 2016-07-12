# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-07-12 15:16
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('reservations', '0005_auto_20160709_0927'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reservations',
            name='author',
            field=models.ForeignKey(default=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='reservations', to=settings.AUTH_USER_MODEL),
        ),
    ]