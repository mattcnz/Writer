# -*- coding: utf-8 -*-
# Generated by Django 1.11rc1 on 2017-06-23 08:30
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.TextField(default='Book One')),
                ('content', models.TextField(default='Some text goes here')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('editable', models.BooleanField(default=True)),
                ('goal', models.IntegerField(default=1000)),
                ('is_finished', models.BooleanField(default=False)),
                ('wordsPerPeriod', models.IntegerField(default=500)),
                ('timePeriod', models.IntegerField(default=30)),
                ('out_of_time', models.BooleanField(default=False)),
                ('time_total', models.IntegerField(default=10000)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='books', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'get_latest_by': 'created_at',
            },
        ),
        migrations.CreateModel(
            name='Library',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(default='New Library')),
                ('books', models.ManyToManyField(related_name='libraries', to='books.Book')),
            ],
        ),
    ]
