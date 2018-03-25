# !/usr/bin/python
# -*-coding:utf-8-*-
import json
from models import *
from django.shortcuts import get_object_or_404
from django.http import HttpResponse
from dss.Serializer import serializer

# Create your views here.

# 表单

# 菜谱列表
def CookBooksView(request):  
    cook_list = CookBooks.objects.all()
    data = serializer(cook_list, output_type='json')
    #return data
    return HttpResponse(data)


# 菜谱详情
def CookBookView(request, **kargs):  
    data = {}
    cook = get_object_or_404(CookBooks, pk=kargs['pk'])
    # data = serializer(cook_list, output_type='json')
    #return data
    data['name'] = cook.name
    data['desc'] = cook.desc
    data['price'] = cook.price
    data['label'] = cook.label
   
    return HttpResponse(json.dumps(data), content_type="application/json")


# 登录
def LoginView(request, **kargs):  
    token = {}
    cook = get_object_or_404(CookBooks, pk=kargs['pk'])
    # data = serializer(cook_list, output_type='json')
    #return data
    data['name'] = cook.name
    data['desc'] = cook.desc
    data['price'] = cook.price
    data['label'] = cook.label
   
    return HttpResponse(json.dumps(data), content_type="application/json")








