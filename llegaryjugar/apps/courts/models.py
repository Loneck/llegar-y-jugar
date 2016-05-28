from __future__ import unicode_literals

from django.db import models
from django.utils.translation import ugettext as _

from llegaryjugar.apps.base.models import BaseModel
from llegaryjugar.apps.clubs.models import Club
from llegaryjugar.apps.schedules.models import Schedule


class CourtManager(models.Manager):
    use_for_related_fields = True

    def active(self):
        return self.get_queryset().filter(is_active=True)


class Court(BaseModel):
    club = models.ForeignKey(Club, related_name='court', verbose_name=_('club'))
    name = models.CharField(_('name'), max_length=50)
    description = models.TextField(_('description'))
    # schedules = models.ManyToManyField(Schedule, verbose_name=_('schedules'))
    is_active = models.BooleanField(_('is active'), default=True)

    def __str__(self):
        return self.name

    objects = CourtManager()


class ScheduleCourt(BaseModel):
    court = models.ForeignKey(Court, related_name='schedule_court', verbose_name=_('court'))
    schedule = models.ForeignKey(Schedule, related_name='schedule_court', verbose_name=_('schedule'))
    price = models.DecimalField(_('price'), decimal_places=2, max_digits=30)
