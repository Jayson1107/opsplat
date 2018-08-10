# -*- coding: utf-8 -*-
# Generated by Django 1.11.9 on 2018-05-29 08:00
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ljapps', '0004_funcexe_rollback'),
    ]

    operations = [
        migrations.CreateModel(
            name='Build_history',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('filename', models.CharField(blank=True, max_length=200)),
                ('dest', models.CharField(blank=True, max_length=20)),
                ('branch', models.CharField(blank=True, max_length=20)),
                ('app', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='ljapps.Apps')),
            ],
        ),
    ]
