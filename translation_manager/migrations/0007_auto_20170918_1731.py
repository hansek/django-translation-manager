# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-09-18 15:31
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('translation_manager', '0006_auto_20170915_1529'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='remotetranslationentry',
            options={'permissions': (('sync', 'admin-translation_entry-sync'),)},
        ),
    ]