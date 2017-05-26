# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-04-26 15:54
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('e2074', '0008_auto_20170426_1050'),
    ]

    operations = [
        migrations.AlterField(
            model_name='candidate',
            name='photo',
            field=models.ImageField(blank=True, null=True, upload_to='images/photo'),
        ),
        migrations.AlterField(
            model_name='party',
            name='logo',
            field=models.ImageField(upload_to='images/logo'),
        ),
    ]
