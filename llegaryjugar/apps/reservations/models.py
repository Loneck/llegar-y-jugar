from __future__ import unicode_literals

from django.db import models
from django.contrib import admin
from django.utils import timezone
from django.utils.translation import ugettext as _
from llegaryjugar.apps.base.models import BaseModel
from llegaryjugar.apps.clubs.models import Club
from llegaryjugar.apps.courts.models import ScheduleCourt
from llegaryjugar.apps.accesorie.models import Accesorie


class Reservations(BaseModel):
    author = models.ForeignKey('auth.User', null=True, default=True)
    club = models.ForeignKey(Club, related_name='club_name', null=True)
    schedule = models.ForeignKey(ScheduleCourt, related_name='schedule_schedule', null=True)
    accesorie = models.ForeignKey(Accesorie, related_name='accesorie', null=True)
    price = models.DecimalField(_('price'), decimal_places=2, max_digits=30, null=True)
    reserved_at = models.DateTimeField(
        auto_now_add=True,
        help_text=_('creation date'),
        null=True,
    )
