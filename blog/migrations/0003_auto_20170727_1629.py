# -*- coding: utf-8 -*-
# Generated by Django 1.11.2 on 2017-07-27 08:29
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_contact_tag'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='age',
            field=models.IntegerField(default=0),
        ),
    ]