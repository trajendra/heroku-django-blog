# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-09-22 11:12
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0011_auto_20160920_1546'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='centre',
            name='school',
        ),
        migrations.RemoveField(
            model_name='school',
            name='campus',
        ),
        migrations.DeleteModel(
            name='Campus',
        ),
        migrations.DeleteModel(
            name='Centre',
        ),
        migrations.DeleteModel(
            name='School',
        ),
    ]
