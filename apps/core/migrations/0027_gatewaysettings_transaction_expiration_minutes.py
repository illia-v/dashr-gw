# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2018-01-09 19:45
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0026_auto_20180109_1052'),
    ]

    operations = [
        migrations.AddField(
            model_name='gatewaysettings',
            name='transaction_expiration_minutes',
            field=models.PositiveIntegerField(default=60, verbose_name='Transaction expiration (minutes)'),
        ),
    ]
