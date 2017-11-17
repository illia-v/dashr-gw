# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-11-17 13:24
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_auto_20171117_1220'),
    ]

    operations = [
        migrations.CreateModel(
            name='DepositTransactionStateChange',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('datetime', models.DateTimeField(auto_created=True)),
                ('current_state', models.PositiveSmallIntegerField(choices=[(1, 'Initiated'), (2, 'In progress'), (3, 'Completed'), (4, 'Not processed'), (5, 'Failed')])),
                ('transaction', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='state_changes', to='core.DepositTransaction')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
