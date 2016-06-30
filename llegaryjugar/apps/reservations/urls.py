# -*- coding: utf-8 -*-
from django.conf import settings
from django.conf.urls import url, include
from django.contrib import admin
from django.conf.urls.static import static
from . import as_view
from llegaryjugar.apps.reservations.views import club_list
from llegaryjugar.apps.reservations.forms import ContactForm1, ContactForm2
from llegaryjugar.apps.reservations.views import ContactWizard

urlpatterns = [
    url(r'^$', views.club_list),
    url(r'^$', ContactWizard.as_view([ContactForm1, ContactForm2])),
]

if settings.DEBUG:
    import debug_toolbar
    urlpatterns += [url(r'^__debug__/', include(debug_toolbar.urls))]
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)