# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2019-03-09 19:28
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resume', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cv',
            name='link',
        ),
        migrations.AddField(
            model_name='cv',
            name='interests',
            field=models.CharField(default='nothing', max_length=500),
        ),
        migrations.AddField(
            model_name='cv',
            name='skills',
            field=models.CharField(default='no thing ', max_length=100),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='cv',
            name='tech_train',
            field=models.CharField(default='no', max_length=500),
            preserve_default=False,
        ),
    ]
