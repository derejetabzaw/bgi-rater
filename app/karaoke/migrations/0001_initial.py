# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2020-11-22 19:14
from __future__ import unicode_literals

from django.db import migrations, models
import karaoke.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='RecordedAudio',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('audio', models.FileField(blank=True, max_length=500, null=True, upload_to=karaoke.models.upload_path)),
            ],
        ),
    ]