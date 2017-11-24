# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-11-22 19:51
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Continent',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=16)),
            ],
            options={
                'ordering': ('name',),
            },
        ),
        migrations.CreateModel(
            name='ExampleForm',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=32)),
                ('last_name', models.CharField(max_length=64)),
                ('date_of_birth', models.DateTimeField()),
                ('email', models.EmailField(max_length=254)),
                ('favourite_number', models.IntegerField()),
                ('your_continent', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='form.Continent')),
            ],
        ),
    ]