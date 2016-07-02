# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-07-02 16:12
from __future__ import unicode_literals

import client.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Client',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Name')),
                ('rg', models.CharField(blank=True, max_length=12, verbose_name='RG')),
                ('cpf', models.CharField(blank=True, max_length=15, validators=[client.models.validate_cpf],
                                         verbose_name='CPF')),
                ('email', models.EmailField(blank=True, max_length=254, null=True, verbose_name='E-mail')),
                ('phone', models.CharField(blank=True, max_length=15, verbose_name='Phone')),
                ('cellphone', models.CharField(blank=True, max_length=15, verbose_name='Cell Phone')),
                ('zipcode', models.CharField(blank=True, max_length=9, verbose_name='Zip Code')),
                ('street', models.CharField(blank=True, max_length=255, verbose_name='Address')),
                ('street_complement', models.CharField(blank=True, max_length=255, verbose_name='Complement')),
                ('number', models.PositiveIntegerField(blank=True, null=True, verbose_name='Number')),
                ('district', models.CharField(blank=True, max_length=255, verbose_name='District')),
                ('city', models.CharField(blank=True, max_length=255, verbose_name='City')),
                ('state', models.CharField(blank=True, max_length=255, verbose_name='State')),
                ('note', models.CharField(blank=True, max_length=255, verbose_name='Note')),
            ],
            options={
                'ordering': ('name',),
                'verbose_name': 'Client',
                'verbose_name_plural': 'Clients',
            },
        ),
        migrations.CreateModel(
            name='ClientContact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=255, verbose_name='Name')),
                ('phone', models.CharField(blank=True, max_length=15, verbose_name='Phone')),
                ('cellphone', models.CharField(blank=True, max_length=15, verbose_name='Cell Phone')),
                ('client_name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='client.Client')),
            ],
            options={
                'verbose_name': 'Client contact',
                'verbose_name_plural': 'Client contacts',
            },
        ),
    ]
