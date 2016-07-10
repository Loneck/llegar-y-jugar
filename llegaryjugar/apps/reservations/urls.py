# -*- coding: utf-8 -*-
from django.conf import settings
from django.conf.urls import url, include, patterns
from django.contrib import admin
from django.conf.urls.static import static
from llegaryjugar.apps.reservations.forms import ClubForm, ScheduleForm, AccesorieForm, PaymentForm
from llegaryjugar.apps.reservations.views import StepWizard


urlpatterns = [
    # url(r'^$', views.club_list),  # Esta URL evita que se ejecute la url de abajo.
    url(r'^$', StepWizard.as_view([ClubForm, ScheduleForm, AccesorieForm, PaymentForm])),
]