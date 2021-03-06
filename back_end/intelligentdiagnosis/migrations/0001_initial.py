# -*- coding: utf-8 -*-
# Generated by Django 1.11.15 on 2019-04-03 03:11
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='IntelligentDiagnosis',
            fields=[
                ('diagnosis_id', models.IntegerField(primary_key=True, serialize=False)),
                ('diagnosis_studyUID', models.CharField(max_length=255)),
                ('diagnosis_seriesUID', models.CharField(max_length=255)),
                ('diagnosis_algorithm', models.CharField(max_length=255)),
                ('diagnosis_time', models.DateTimeField(default=django.utils.timezone.now)),
                ('diagnosis_info', models.TextField()),
            ],
        ),
    ]
