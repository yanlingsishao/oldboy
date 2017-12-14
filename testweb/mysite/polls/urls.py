#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2017-11-10 17:13
# @Author  : Jerry Wang
# @Site    : 
# @File    : urls.py
# @Software: PyCharm
from django.conf.urls import include, url
from django.contrib import admin

from django.conf.urls import url

from . import views

urlpatterns = [
    # ex: /polls/
    url(r'^$', views.index, name='index'),
    # ex: /polls/5/
    url(r'^(?P<question_id>[0-9]+)/$', views.detail, name='detail'),
    # ex: /polls/5/results/
    url(r'^(?P<question_id>[0-9]+)/results/$', views.results, name='results'),
    # ex: /polls/5/vote/
    url(r'^(?P<question_id>[0-9]+)/vote/$', views.vote, name='vote'),
]