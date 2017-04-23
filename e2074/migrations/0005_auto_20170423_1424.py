# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-04-23 14:24
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('e2074', '0004_auto_20170423_1324'),
    ]

    operations = [
        migrations.AddField(
            model_name='district',
            name='municipality',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='district',
            name='population',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='district',
            name='vdc',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='district',
            name='voters',
            field=models.IntegerField(default=1),
            preserve_default=False,
        ),
    ]