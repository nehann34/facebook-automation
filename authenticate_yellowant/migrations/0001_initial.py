# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2018-03-26 18:46
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='yellowant_table',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('yellowant_token', models.CharField(max_length=100)),
                ('yellowant_id', models.IntegerField(default=0)),
                ('yellowant_integration_id', models.IntegerField(default=0)),
            ],
        ),
    ]