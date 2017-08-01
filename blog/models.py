# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from __future__ import unicode_literals

from django.db import models


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class Tb20161130(models.Model):
    xuhao = models.CharField(max_length=8)
    editor = models.CharField(max_length=50)
    banming = models.CharField(max_length=16)
    title = models.CharField(max_length=45)
    imgsrc = models.CharField(max_length=80)
    body = models.TextField()

    class Meta:
        managed = False
        db_table = 'tb_2016_11_30'


class Tb20170801(models.Model):
    xuhao = models.CharField(max_length=8)
    editor = models.CharField(max_length=50)
    banming = models.CharField(max_length=16)
    title = models.CharField(max_length=45)
    imgsrc = models.CharField(max_length=80)
    body = models.TextField()

    class Meta:
        managed = False
        db_table = 'tb_2017_08_01'
