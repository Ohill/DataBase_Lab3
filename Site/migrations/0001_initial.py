# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-10-21 20:31
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, default=None, max_length=15, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Site',
            fields=[
                ('Site_id', models.IntegerField(primary_key=True, serialize=False)),
                ('Site_Name', models.CharField(blank=True, default=None, max_length=48, null=True)),
                ('Site_Category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Site.Category')),
            ],
        ),
    ]
