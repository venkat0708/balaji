# -*- coding: utf-8 -*-
# Generated by Django 1.9.4 on 2016-11-08 18:03
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounting', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='type',
            field=models.CharField(choices=[('Income', 'Income'), ('Expense', 'Expense'), ('Liability', 'Liability')], default='Income', max_length=30),
        ),
    ]
