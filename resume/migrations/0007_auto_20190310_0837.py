# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2019-03-10 08:37
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('resume', '0006_auto_20190309_2025'),
    ]

    operations = [
        migrations.CreateModel(
            name='interest',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('interests', models.CharField(max_length=500)),
            ],
        ),
        migrations.CreateModel(
            name='skill',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('skills', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='train',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('trains', models.CharField(max_length=5000)),
            ],
        ),
        migrations.DeleteModel(
            name='cv',
        ),
    ]