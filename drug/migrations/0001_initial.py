# -*- coding: utf-8 -*-
# Generated by Django 1.11.11 on 2018-12-31 19:51
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('animal', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Classification',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Name')),
            ],
            options={
                'verbose_name': 'Classification',
                'verbose_name_plural': 'Classifications',
                'ordering': ('name',),
            },
        ),
        migrations.CreateModel(
            name='Drug',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('generic_name', models.CharField(max_length=150)),
                ('commercial_name', models.CharField(blank=True, max_length=150)),
                ('use', models.CharField(blank=True, choices=[('human', 'Human'), ('pediatric', 'Human pediatric'), ('vet', 'Vet')], default=None, max_length=10)),
                ('value', models.CharField(max_length=10)),
                ('value_for', models.CharField(max_length=10)),
                ('classification', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='drug.Classification')),
            ],
            options={
                'verbose_name': 'Drug',
                'verbose_name_plural': 'Drugs',
                'ordering': ('generic_name',),
            },
        ),
        migrations.CreateModel(
            name='DrugDosage',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value_from', models.CharField(max_length=10)),
                ('value_to', models.CharField(blank=True, max_length=10)),
                ('value_for', models.CharField(default=1, max_length=10)),
                ('periodicity', models.CharField(max_length=10)),
                ('period', models.CharField(max_length=10)),
                ('drug', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='drug.Drug')),
            ],
            options={
                'verbose_name': 'Drug dosage',
                'verbose_name_plural': 'Drugs dosage',
                'ordering': ('drug',),
            },
        ),
        migrations.CreateModel(
            name='Group',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Name')),
            ],
            options={
                'verbose_name': 'Group',
                'verbose_name_plural': 'Groups',
                'ordering': ('name',),
            },
        ),
        migrations.CreateModel(
            name='Indication',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Name')),
            ],
            options={
                'verbose_name': 'Indication',
                'verbose_name_plural': 'Indications',
                'ordering': ('name',),
            },
        ),
        migrations.CreateModel(
            name='Manufacturer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Name')),
            ],
            options={
                'verbose_name': 'Manufacturer',
                'verbose_name_plural': 'Manufacturers',
                'ordering': ('name',),
            },
        ),
        migrations.CreateModel(
            name='Presentation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Name')),
            ],
            options={
                'verbose_name': 'Presentation',
                'verbose_name_plural': 'Presentations',
                'ordering': ('name',),
            },
        ),
        migrations.CreateModel(
            name='System',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, verbose_name='Name')),
            ],
            options={
                'verbose_name': 'System',
                'verbose_name_plural': 'Systems',
                'ordering': ('name',),
            },
        ),
        migrations.CreateModel(
            name='UnitOfMeasurement',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Name')),
                ('abbreviation', models.CharField(max_length=10, verbose_name='Abbreviation')),
                ('system', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='drug.System', verbose_name='System')),
            ],
            options={
                'verbose_name': 'Unit of measurement',
                'verbose_name_plural': 'Units of measurement',
                'ordering': ('name',),
            },
        ),
        migrations.AddField(
            model_name='drugdosage',
            name='period_unit',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='dosage_period', to='drug.UnitOfMeasurement'),
        ),
        migrations.AddField(
            model_name='drugdosage',
            name='periodicity_unit',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='dosage_periodicity', to='drug.UnitOfMeasurement'),
        ),
        migrations.AddField(
            model_name='drugdosage',
            name='specie',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='animal.Specie'),
        ),
        migrations.AddField(
            model_name='drugdosage',
            name='value_for_unit',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='dosage_value_for_unit', to='drug.UnitOfMeasurement'),
        ),
        migrations.AddField(
            model_name='drugdosage',
            name='value_unit',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='dosage_value_unit', to='drug.UnitOfMeasurement'),
        ),
        migrations.AddField(
            model_name='drug',
            name='group',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='drug.Group'),
        ),
        migrations.AddField(
            model_name='drug',
            name='indication',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='drug.Indication'),
        ),
        migrations.AddField(
            model_name='drug',
            name='manufacturer',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='drug.Manufacturer'),
        ),
        migrations.AddField(
            model_name='drug',
            name='presentation',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='drug.Presentation'),
        ),
        migrations.AddField(
            model_name='drug',
            name='value_for_unit',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='drug_value_for_unit', to='drug.UnitOfMeasurement'),
        ),
        migrations.AddField(
            model_name='drug',
            name='value_unit',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='drug_value_unit', to='drug.UnitOfMeasurement'),
        ),
    ]