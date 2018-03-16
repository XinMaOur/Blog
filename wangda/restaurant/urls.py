# -*- coding: utf-8 -*-

from views import *
from django.conf.urls import url

urlpatterns = [
    url(r'^cookbooks/$', CookBooksView, name='cookbooks'),
    url(r'^cookbook/(?P<pk>[0-9]+)/$', CookBookView, name='cookbook')
    
]