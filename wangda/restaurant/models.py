# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.


class CookBooks(models.Model):
    name = models.CharField(max_length=150, db_index=True, unique=True)
    desc = models.TextField()
    price = models.IntegerField(db_index=True)
    label =  models.CharField(max_length=150, blank=True, null=True, db_index=True)

class User(models.Model):
    UNKNOWN ,BOY, GIRL = range(0, 3)
    GENDER_CHOICES =(
        (UNKNOWN, 'unknown'),
        (BOY, 'boy'),
        (GIRL, 'girl')
    )

    nickName = models.CharField(max_length=150, db_index=True)
    avatarUrl = models.URLField(null=True, blank=True)
    gender = models.CharField(
        max_length=2,
        choices=GENDER_CHOICES
    )
    city = models.CharField(max_length=150, db_index=True)
    province = models.CharField(max_length=150, db_index=True)
    country = models.CharField(max_length=150, db_index=True)
    lastLogin = models.DateTimeField(auto_now=True)