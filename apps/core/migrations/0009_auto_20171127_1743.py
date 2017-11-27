# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-11-27 17:43
from __future__ import unicode_literals

from django.db import migrations, models
import django_fsm


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0008_auto_20171123_1918'),
    ]

    operations = [
        migrations.AlterField(
            model_name='deposittransaction',
            name='state',
            field=django_fsm.FSMIntegerField(choices=[(1, 'Initiated'), (2, 'Received an incoming transaction (hash - {incoming_dash_transaction_hash}). Waiting for {confirmations_number} confirmations'), (3, 'Confirmed the incoming transaction (hash - {incoming_dash_transaction_hash}). Initiated an outgoing one'), (4, 'Transaction is processed. Hash of a Ripple transaction is {outgoing_ripple_transaction_hash}'), (5, 'Received 0 Dash transactions. Transactions to the address {dash_address} are no longer tracked'), (6, 'Transaction failed. Please contact our support team')], default=1),
        ),
        migrations.AlterField(
            model_name='deposittransactionstatechange',
            name='current_state',
            field=models.PositiveSmallIntegerField(choices=[(1, 'Initiated'), (2, 'Received an incoming transaction (hash - {incoming_dash_transaction_hash}). Waiting for {confirmations_number} confirmations'), (3, 'Confirmed the incoming transaction (hash - {incoming_dash_transaction_hash}). Initiated an outgoing one'), (4, 'Transaction is processed. Hash of a Ripple transaction is {outgoing_ripple_transaction_hash}'), (5, 'Received 0 Dash transactions. Transactions to the address {dash_address} are no longer tracked'), (6, 'Transaction failed. Please contact our support team')]),
        ),
    ]
