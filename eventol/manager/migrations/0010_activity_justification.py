# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2018-04-18 04:44
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('manager', '0009_auto_20180413_0420'),
    ]

    operations = [
        migrations.AddField(
            model_name='activity',
            name='justification',
            field=models.TextField(blank=True, help_text='Why do you reject this proposal?', null=True, verbose_name='Justification'),
        ),
    ]
