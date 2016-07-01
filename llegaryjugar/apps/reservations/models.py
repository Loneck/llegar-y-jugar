from __future__ import unicode_literals

from django.db import models
from django.contrib import admin
from django.utils.translation import ugettext as _

from llegaryjugar.apps.base.models import BaseModel
from llegaryjugar.apps.clubs.models import Club
from llegaryjugar.apps.schedules.models import Schedule
from llegaryjugar.apps.courts.models import ScheduleCourt
from llegaryjugar.apps.accesorie.models import Accesorie


class Reservations(BaseModel):
    res_schedule = models.ForeignKey(ScheduleCourt, related_name='res_schedule_schedule', verbose_name=_('scheduleCourt'), null=True)
    res_club = models.ForeignKey(Club, related_name='res_name', null=True) 
    res_court = models.ForeignKey(ScheduleCourt, related_name='res_schedule_court', null=True)
    res_accesorie = models.ForeignKey(Accesorie, related_name='res_accesorie', null=True)
    res_price = models.ForeignKey(ScheduleCourt, related_name='res_schedule_price', null=True)

    
