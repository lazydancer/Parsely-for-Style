# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-07-27 23:38
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('plan', '0004_auto_20170727_1916'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ingredient',
            name='component',
        ),
        migrations.DeleteModel(
            name='Component',
        ),
    ]
