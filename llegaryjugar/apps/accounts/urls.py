# -*- coding: utf-8 -*-
from django.conf.urls import patterns, url
from django.contrib.auth import views as auth_views
from .import views


urlpatterns = [
	url(r'profile/$', views.profile_detail_view, name='profile_detail_view'),
	url(r'profile/edit/$', views.profile_edit_view, name='profile_edit_view'),
]