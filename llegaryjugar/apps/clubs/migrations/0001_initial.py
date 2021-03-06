# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-05-28 21:58
from __future__ import unicode_literals

import ajaximage.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Club',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, help_text='creation date')),
                ('updated_at', models.DateTimeField(auto_now=True, help_text='edition date', null=True)),
                ('name', models.CharField(max_length=50, verbose_name='nombre')),
                ('address', models.CharField(max_length=50, verbose_name='address')),
                ('description', models.TextField(verbose_name='descripci\xf3n')),
                ('logo', ajaximage.fields.AjaxImageField(verbose_name='image')),
                ('is_active', models.BooleanField(default=True, verbose_name='is active')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
