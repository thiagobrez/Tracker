# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-07-25 00:51
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clock', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200, unique=True)),
                ('start', models.DateTimeField()),
                ('end', models.DateTimeField()),
                ('duration', models.DateTimeField()),
            ],
        ),
    ]