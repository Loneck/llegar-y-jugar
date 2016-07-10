# -*- coding: utf-8 -*-
from django.conf.urls import patterns, url
from django.contrib.auth import views as auth_views


urlpatterns = patterns('accounts.views',
	url(r'profile/$', 'profile_detail_view', name='profile_detail_view'),
	url(r'profile/edit/$', 'profile_edit_view', name='profile_edit_view'),
)