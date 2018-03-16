# -*- coding: utf-8 -*-
#!/usr/bin/env python

from rest_framework import pagination
from django.utils.translation import ugettext_lazy as _

class CommonPagination(pagination.PageNumberPagination):
    max_page_size = 100
    page_size_query_param = 'size'
    page_size = 10