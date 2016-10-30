#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^all/', views.all, name='all'),
    url(r'^title/(?P<anime_title>.+)/', views.anime_details, name='title'),
]



















