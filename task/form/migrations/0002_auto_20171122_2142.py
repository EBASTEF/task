# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-22 21:42
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('form', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='exampleform',
            name='your_continent',
        ),
        migrations.DeleteModel(
            name='Continent',
        ),
        migrations.DeleteModel(
            name='ExampleForm',
        ),
    ]
