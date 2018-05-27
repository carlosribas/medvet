# -*- coding: utf-8 -*-
# Generated by Django 1.9.13 on 2018-05-26 02:42
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('animal', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='AmbulatoryService',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
            ],
        ),
        migrations.CreateModel(
            name='ConsultationType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
            ],
        ),
        migrations.CreateModel(
            name='ExamType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
            ],
        ),
        migrations.CreateModel(
            name='Service',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('service_type', models.CharField(choices=[(b'consultation', 'Consultation'), (b'surgery', 'Surgical procedure'), (b'vaccine', 'Vaccine'), (b'exams', 'Exams'), (b'ambulatory', 'Ambulatory services')], max_length=20)),
                ('date', models.DateField(default=datetime.date.today)),
            ],
        ),
        migrations.CreateModel(
            name='SurgicalProcedure',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
            ],
        ),
        migrations.CreateModel(
            name='VaccineType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('price', models.DecimalField(decimal_places=2, max_digits=10)),
            ],
        ),
        migrations.CreateModel(
            name='Ambulatory',
            fields=[
                ('service_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='services.Service')),
                ('ambulatory_service_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='services.AmbulatoryService')),
            ],
            bases=('services.service',),
        ),
        migrations.CreateModel(
            name='Consultation',
            fields=[
                ('service_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='services.Service')),
                ('title', models.CharField(blank=True, max_length=255, verbose_name='Title')),
                ('temperature', models.CharField(blank=True, max_length=3, verbose_name='Temperature')),
                ('bodyweight', models.CharField(blank=True, max_length=10, verbose_name='Bodyweight')),
                ('body_condition', models.CharField(blank=True, choices=[(b'0', '1 - Very thin'), (b'1', '2 - Underweight'), (b'2', '3 - Ideal weight'), (b'3', '4 - Overweight'), (b'4', '5 - Obese')], max_length=1, verbose_name='Body Condition Score')),
                ('hydration', models.CharField(blank=True, choices=[(b'no_dehydration', 'No dehydration'), (b'reports_loss_of_liquids', 'Less than 5% - Reports loss of liquids'), (b'mild', '5 to 6% - Mild'), (b'moderate', '7 to 9% - Moderate'), (b'severe', '10 to 12% - Severe'), (b'hypovolemic_shock', '12 to 15% - Hypovolemic shock')], max_length=25, verbose_name='Skin Tenting')),
                ('mucous_membrane', models.CharField(blank=True, choices=[(b'pink', 'Pink'), (b'blue', 'Blue'), (b'pale', 'Pale'), (b'icteric', 'Icteric'), (b'congested', 'Congested')], max_length=10, verbose_name='Mucous Membrane')),
                ('palpable_thyroid', models.CharField(blank=True, choices=[(b'normal', 'Normal'), (b'abnormal', 'Abnormal')], max_length=10, verbose_name='Palpable Thyroid')),
                ('palpable_thyroid_note', models.CharField(blank=True, max_length=255, verbose_name='Note')),
                ('auscultation', models.CharField(blank=True, choices=[(b'normal', 'Normal'), (b'abnormal', 'Abnormal')], max_length=10, verbose_name='Auscultation')),
                ('auscultation_note', models.CharField(blank=True, max_length=255, verbose_name='Note')),
                ('abdominal_palpation', models.CharField(blank=True, choices=[(b'normal', 'Normal'), (b'abnormal', 'Abnormal')], max_length=10, verbose_name='Abdominal Palpation')),
                ('abdominal_palpation_note', models.CharField(blank=True, max_length=255, verbose_name='Note')),
                ('additional_findings', models.TextField(blank=True, verbose_name='Note')),
                ('consultation_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='services.ConsultationType')),
            ],
            bases=('services.service',),
        ),
        migrations.CreateModel(
            name='Exams',
            fields=[
                ('service_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='services.Service')),
                ('exam_file', models.FileField(blank=True, null=True, upload_to=b'exams/')),
                ('note', models.TextField(blank=True)),
                ('exam_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='services.ExamType')),
            ],
            bases=('services.service',),
        ),
        migrations.CreateModel(
            name='Surgery',
            fields=[
                ('service_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='services.Service')),
                ('procedure_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='services.SurgicalProcedure')),
            ],
            bases=('services.service',),
        ),
        migrations.CreateModel(
            name='Vaccine',
            fields=[
                ('service_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='services.Service')),
                ('lot', models.CharField(blank=True, max_length=255)),
                ('booster', models.DateField(blank=True, null=True)),
                ('note', models.TextField(blank=True)),
                ('vaccine_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='services.VaccineType')),
            ],
            bases=('services.service',),
        ),
        migrations.AddField(
            model_name='service',
            name='animal',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='animal.Animal'),
        ),
    ]
