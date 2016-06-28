from django import forms

from django.db import models
from django.contrib import admin
from django.utils.translation import ugettext as _

from llegaryjugar.apps.clubs.models import Club
from llegaryjugar.apps.courts.models import ScheduleCourt
from llegaryjugar.apps.schedules.models import Schedule

class LoginForm(forms.Form):
	username = forms.CharField()
	password = forms.CharField(widget = forms.PasswordInput())


class StepForm1(forms.Form):
    club = models.ForeignKey(Club, related_name='court', verbose_name=_('club'))

class StepForm2(forms.Form):
    scheduleCourt = models.ForeignKey(Schedule, related_name='schedule_courtyard', verbose_name=_('schedule'))

class StepForm3(forms.Form):
    message = forms.CharField(max_length=100)

class StepForm4(forms.Form):
    message = forms.CharField(max_length=100)      
