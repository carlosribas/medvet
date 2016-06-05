# -*- coding: utf-8 -*-
# Generated by Django 1.9.6 on 2016-06-04 23:29
from __future__ import unicode_literals

import animal.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('client', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Animal',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fur', models.CharField(blank=True, choices=[(b'l', 'Long'), (b's', 'Short')], max_length=1, null=True, verbose_name='Fur')),
                ('animal_name', models.CharField(error_messages={b'required': 'Please enter the name of the pet'}, max_length=100, verbose_name="Animal's Name")),
                ('birthdate', models.DateField(blank=True, null=True, validators=[animal.models.validate_date_birth], verbose_name='Birthdate')),
                ('sex', models.CharField(blank=True, choices=[(b'm', 'Male'), (b'f', 'Female')], max_length=1, null=True, verbose_name='Sex')),
                ('spay_neuter', models.CharField(blank=True, choices=[(b'n', 'No'), (b'y', 'Yes')], max_length=1, null=True, verbose_name='Spay or Neuter')),
                ('spay_neuter_date', models.CharField(blank=True, max_length=100, null=True, verbose_name='When?')),
                ('microchip', models.CharField(blank=True, max_length=50, null=True, verbose_name='Microchip')),
                ('dead', models.BooleanField(default=False, verbose_name='Dead')),
                ('note', models.CharField(blank=True, max_length=255, null=True, verbose_name='Note')),
            ],
            options={
                'ordering': ('animal_name',),
                'verbose_name': 'Animal',
                'verbose_name_plural': 'Animals',
            },
        ),
        migrations.CreateModel(
            name='Breed',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Name')),
            ],
            options={
                'ordering': ('name',),
                'verbose_name': 'Breed',
                'verbose_name_plural': 'Breeds',
            },
        ),
        migrations.CreateModel(
            name='Color',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Name')),
            ],
            options={
                'ordering': ('name',),
                'verbose_name': 'Color',
                'verbose_name_plural': 'Colors',
            },
        ),
        migrations.CreateModel(
            name='Specie',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Name')),
            ],
            options={
                'ordering': ('name',),
                'verbose_name': 'Specie',
                'verbose_name_plural': 'Species',
            },
        ),
        migrations.AddField(
            model_name='color',
            name='specie',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='animal.Specie', verbose_name='Specie'),
        ),
        migrations.AddField(
            model_name='breed',
            name='specie',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='animal.Specie', verbose_name='Specie'),
        ),
        migrations.AddField(
            model_name='animal',
            name='breed',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='animal.Breed', verbose_name='Breed'),
        ),
        migrations.AddField(
            model_name='animal',
            name='color',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='animal.Color', verbose_name='Color'),
        ),
        migrations.AddField(
            model_name='animal',
            name='owner',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='client.Client', verbose_name='Owner'),
        ),
    ]
