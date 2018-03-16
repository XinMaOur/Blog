# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.


class CookBooks(models.Model):
    name = models.CharField(max_length=150, db_index=True, unique=True)
    desc = models.TextField()
    price = models.IntegerField(db_index=True)
    label =  models.CharField(max_length=150, blank=True, null=True, db_index=True)