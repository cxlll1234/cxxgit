# -*- coding: utf-8 -*-
# Generated by Django 1.9.13 on 2017-05-20 02:20
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='T_USER',
            fields=[
                ('user_id', models.CharField(max_length=8, primary_key=True, serialize=False)),
                ('user_name', models.CharField(max_length=20)),
                ('user_password', models.CharField(max_length=100)),
                ('user_status', models.CharField(max_length=1)),
            ],
        ),
    ]
