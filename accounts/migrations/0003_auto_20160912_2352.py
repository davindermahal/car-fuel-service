# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2016-09-12 23:52
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_remove_myprofile_favourite_snack'),
    ]

    operations = [
        migrations.AlterField(
            model_name='myprofile',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, parent_link=True, related_name='my_profile', to=settings.AUTH_USER_MODEL, verbose_name='user'),
        ),
    ]