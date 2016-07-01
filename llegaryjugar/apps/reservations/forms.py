from django import forms

from django.db import models
from django.contrib import admin
from django.utils.translation import ugettext as _

from llegaryjugar.apps.clubs.models import Club
from llegaryjugar.apps.courts.models import ScheduleCourt
from llegaryjugar.apps.schedules.models import Schedule

# class StepForm1(forms.Form):
#     club = models.ForeignKey(Club, related_name='court', verbose_name=_('club'))

# class StepForm2(forms.Form):
#     scheduleCourt = models.ForeignKey(Schedule, related_name='schedule_courtyard', verbose_name=_('schedule'))

# class StepForm3(forms.Form):
#     message = forms.CharField(max_length=100)

# class StepForm4(forms.Form):
#     message = forms.CharField(max_length=100)

class ClubForm(forms.Form):
    subject = forms.CharField(max_length=100)
    sender = forms.EmailField()

class ScheduleForm(forms.Form):
    message = forms.CharField(widget=forms.Textarea)

class AccesorieForm(forms.Form):
    message2 = forms.CharField(widget=forms.Textarea)

class PaymentForm(forms.Form):
    message3 = forms.CharField(widget=forms.Textarea)    