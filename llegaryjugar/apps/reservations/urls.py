# -*- coding: utf-8 -*-
from django.conf import settings
from django.conf.urls import url, include
from django.contrib import admin
from django.conf.urls.static import static
from llegaryjugar.apps.reservations.forms import StepForm1, StepForm2, StepForm3, StepForm4
from llegaryjugar.apps.reservations.views import StepWizard

urlpatterns = [
    # url(r'^inicio/', StepWizard.as_view([StepForm1, StepForm2, StepForm3, StepForm4])),
]

if settings.DEBUG:
    import debug_toolbar
    urlpatterns += [url(r'^__debug__/', include(debug_toolbar.urls))]
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)