# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-02-27 10:24
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0002_auto_20170227_0913'),
    ]

    operations = [
        migrations.RenameField(
            model_name='dashboard',
            old_name='username',
            new_name='name',
        ),
    ]
