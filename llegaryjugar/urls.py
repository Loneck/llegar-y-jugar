# -*- coding: utf-8 -*-
from django.conf import settings
from django.conf.urls import url, include
from django.contrib import admin
from django.conf.urls.static import static
from llegaryjugar.forms import StepForm1, StepForm2, StepForm3, StepForm4
from llegaryjugar.views import StepWizard

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^ajaximage/', include('ajaximage.urls')),
    # url(r'^inicio/', include('inicio.urls')),
    # url(r'^recinto/', include('recinto.urls')),
    url(r'^', include('inicio.urls')),
    url(r'^login/', 'llegaryjugar.views.login_page', name="Login"),
    url(r'^inicio/', StepWizard.as_view([StepForm1, StepForm2, StepForm3, StepForm4])),
]

admin.site.site_header = 'Administración de Llegar y Jugar'

if settings.DEBUG:
    import debug_toolbar
    urlpatterns += [url(r'^__debug__/', include(debug_toolbar.urls))]
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)