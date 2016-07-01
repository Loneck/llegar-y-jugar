# -*- coding: utf-8 -*-
from django.conf import settings
from django.conf.urls import url, include, patterns
from django.contrib import admin
from django.conf.urls.static import static
from llegaryjugar.apps.reservations.views import club_list
from llegaryjugar.apps.reservations.forms import ClubForm, ScheduleForm, AccesorieForm, PaymentForm
from llegaryjugar.apps.reservations.views import ContactWizard

urlpatterns = [
    # url(r'^$', views.club_list),  # Esta URL evita que se ejecute la url de abajo.
    url(r'^$', ContactWizard.as_view([ClubForm, ScheduleForm, AccesorieForm, PaymentForm])),
]