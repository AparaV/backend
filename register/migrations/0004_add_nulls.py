# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2017-06-26 17:57
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('register', '0003_invited_by_foreign'),
    ]

    operations = [
        migrations.AlterField(
            model_name='application',
            name='teammates',
            field=models.CharField(blank=True, max_length=300, null=True),
        ),
    ]