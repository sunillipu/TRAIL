# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2019-04-22 12:02
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Employee_Enquiry_Data',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=50)),
                ('mobile_no', models.BigIntegerField()),
                ('qualification', models.CharField(max_length=50)),
                ('location', models.CharField(max_length=50)),
                ('skill', models.CharField(max_length=50)),
            ],
        ),
    ]
