# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-07-25 22:08
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clock', '0002_project'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='duration',
            field=models.DateTimeField(null=True),
        ),
        migrations.AlterField(
            model_name='project',
            name='end',
            field=models.DateTimeField(null=True),
        ),
    ]
