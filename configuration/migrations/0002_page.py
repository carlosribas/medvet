# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2018-07-02 16:30
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('configuration', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Page',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pagination', models.IntegerField(default=10, verbose_name='Pagination')),
            ],
            options={
                'verbose_name': 'Page',
            },
        ),
    ]