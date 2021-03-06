# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-10-29 16:31
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField(null=True)),
                ('comments', models.TextField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Room',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64)),
                ('capacity', models.IntegerField(null=True)),
                ('description', models.TextField(null=True)),
                ('projector', models.IntegerField(choices=[(1, 'dostepny'), (2, 'brak')], null=True)),
            ],
        ),
        migrations.AddField(
            model_name='booking',
            name='room',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='room', to='app.Room'),
        ),
    ]
