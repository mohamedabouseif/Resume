# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2019-03-13 15:43
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('resume', '0009_auto_20190311_1157'),
    ]

    operations = [
        migrations.RenameField(
            model_name='tech_train',
            old_name='tech_train',
            new_name='tech_train_url',
        ),
    ]
