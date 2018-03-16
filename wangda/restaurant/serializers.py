# !/usr/bin/python
# -*-coding:utf-8-*-
from models import *
from rest_framework import serializers



class CookBooksSerializer(serializers.ModelSerializer):

    class Meta:
        model = CookBooks
        fields = ('id', 'name', 'desc', 'price','label')
        read_only_fields = fields
