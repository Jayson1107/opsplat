# -*- coding: utf-8 -*-
# Generated by Django 1.11.9 on 2018-04-26 02:45
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0008_alter_user_username_max_length'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Action',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('actionname', models.CharField(max_length=40)),
                ('status', models.CharField(default=0, max_length=10)),
                ('output', models.TextField(blank=True, max_length=10000)),
            ],
        ),
        migrations.CreateModel(
            name='Approval',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('approvalname', models.CharField(blank=True, max_length=50)),
                ('user', models.ManyToManyField(blank=True, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Apps',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('appname', models.CharField(max_length=200, unique=True)),
                ('jdkversion', models.CharField(blank=True, max_length=50)),
                ('tomcatversion', models.CharField(blank=True, max_length=50)),
                ('now', models.CharField(blank=True, max_length=200)),
                ('rb1', models.CharField(blank=True, max_length=200)),
                ('rb2', models.CharField(blank=True, max_length=200)),
                ('zipprd', models.CharField(blank=True, max_length=200)),
                ('tv', models.CharField(blank=True, max_length=200)),
                ('ziptest', models.CharField(blank=True, max_length=200)),
                ('pv', models.CharField(blank=True, max_length=200)),
                ('prenow', models.CharField(blank=True, max_length=200)),
                ('prerb1', models.CharField(blank=True, max_length=200)),
                ('prerb2', models.CharField(blank=True, max_length=200)),
                ('zippre', models.CharField(blank=True, max_length=200)),
                ('lock', models.CharField(default=0, max_length=200)),
                ('stats', models.CharField(default=0, max_length=10)),
                ('versionmanage', models.CharField(blank=True, max_length=10)),
                ('versionurl', models.CharField(blank=True, max_length=200)),
                ('targetpath', models.CharField(blank=True, max_length=200)),
                ('appv', models.CharField(blank=True, max_length=200)),
                ('testlock', models.CharField(default=0, max_length=10)),
                ('prelock', models.CharField(default=0, max_length=10)),
                ('prdlock', models.CharField(default=0, max_length=10)),
                ('appsgroup', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='auth.Group')),
            ],
        ),
        migrations.CreateModel(
            name='Apps_history',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('versions', models.CharField(blank=True, max_length=200)),
                ('use_time', models.DateTimeField(default=django.utils.timezone.now, verbose_name='\u4e0a\u7ebf\u65e5\u671f')),
                ('app', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='ljapps.Apps')),
            ],
        ),
        migrations.CreateModel(
            name='Apptype',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('typename', models.CharField(max_length=200, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Balance',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('balance_type', models.CharField(max_length=200)),
                ('balance_name', models.CharField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Balance_attr',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('balance_vip', models.CharField(blank=True, max_length=200)),
                ('balance_port', models.CharField(blank=True, max_length=200)),
                ('app', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='ljapps.Apps')),
                ('balance', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='ljapps.Balance')),
            ],
        ),
        migrations.CreateModel(
            name='Funcevent',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('create_time', models.DateTimeField(blank=True, null=True)),
                ('exec_time', models.DateTimeField(blank=True, null=True)),
                ('end_time', models.DateTimeField(blank=True, null=True)),
                ('exeuser', models.CharField(blank=True, max_length=50)),
                ('event_over', models.BooleanField(default=False)),
                ('eventtype', models.CharField(blank=True, max_length=20)),
                ('status', models.CharField(blank=True, max_length=10)),
                ('destenv', models.CharField(blank=True, max_length=10)),
                ('app', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='ljapps.Apps')),
            ],
        ),
        migrations.CreateModel(
            name='Funcexe',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('exec_time', models.DateTimeField(blank=True, null=True)),
                ('status', models.CharField(blank=True, max_length=10)),
                ('success', models.NullBooleanField()),
                ('output', models.TextField(blank=True, max_length=20000)),
                ('funcevent', models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='ljapps.Funcevent')),
            ],
        ),
        migrations.CreateModel(
            name='Host',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hostip', models.CharField(max_length=200, unique=True)),
                ('lock', models.CharField(default=0, max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Idc',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('idcname', models.CharField(max_length=100, unique=True)),
                ('num', models.CharField(default=0, max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Line',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('line_name', models.CharField(max_length=100, unique=True, verbose_name='\u540d\u79f0')),
                ('line_level', models.IntegerField(default=0, verbose_name='\u7b49\u7ea7')),
            ],
        ),
        migrations.CreateModel(
            name='Ostype',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ostype', models.CharField(max_length=100, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Ports',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('portnum', models.CharField(max_length=50)),
                ('comment', models.CharField(max_length=200)),
                ('app', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ljapps.Apps')),
            ],
        ),
        migrations.CreateModel(
            name='Porttype',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('porttype', models.CharField(max_length=30, unique=True)),
            ],
        ),
        migrations.AddField(
            model_name='ports',
            name='porttype',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ljapps.Porttype'),
        ),
        migrations.AddField(
            model_name='host',
            name='idc',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='ljapps.Idc'),
        ),
        migrations.AddField(
            model_name='host',
            name='line',
            field=models.ManyToManyField(blank=True, to='ljapps.Line'),
        ),
        migrations.AddField(
            model_name='host',
            name='os_group',
            field=models.ManyToManyField(blank=True, to='auth.Group'),
        ),
        migrations.AddField(
            model_name='host',
            name='os_user',
            field=models.ManyToManyField(blank=True, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='host',
            name='ostype',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='ljapps.Ostype'),
        ),
        migrations.AddField(
            model_name='funcexe',
            name='host',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ljapps.Host'),
        ),
        migrations.AddField(
            model_name='balance_attr',
            name='idc',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ljapps.Idc'),
        ),
        migrations.AddField(
            model_name='balance_attr',
            name='line',
            field=models.ManyToManyField(blank=True, to='ljapps.Line'),
        ),
        migrations.AddField(
            model_name='apps',
            name='apptype',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='ljapps.Apptype'),
        ),
        migrations.AddField(
            model_name='apps',
            name='prdhost',
            field=models.ManyToManyField(blank=True, related_name='prd_host', to='ljapps.Host'),
        ),
        migrations.AddField(
            model_name='apps',
            name='prehost',
            field=models.ManyToManyField(blank=True, related_name='pre_host', to='ljapps.Host'),
        ),
        migrations.AddField(
            model_name='apps',
            name='testhost',
            field=models.ManyToManyField(blank=True, related_name='test_host', to='ljapps.Host'),
        ),
        migrations.AddField(
            model_name='apps',
            name='user',
            field=models.ManyToManyField(blank=True, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='action',
            name='app',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='ljapps.Apps'),
        ),
    ]
