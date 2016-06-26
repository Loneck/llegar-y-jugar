from __future__ import unicode_literals

from django.db import models
from django.utils.translation import ugettext as _

from llegaryjugar.apps.base.models import BaseModel
from llegaryjugar.apps.clubs.models import Club
from llegaryjugar.apps.schedules.models import Schedule
from llegaryjugar.apps.courts.models import ScheduleCourt


class Reservations(BaseModel):
	ScheduleCourt = models.ForeignKey(ScheduleCourt, related_name='schedule_court', verbose_name=_('court'))

	list_display = ('club','name','date','day', 'price')
