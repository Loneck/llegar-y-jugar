from __future__ import unicode_literals

from django.db import models
from django.utils.translation import ugettext as _

from llegaryjugar.apps.base.models import BaseModel
from llegaryjugar.apps.clubs.models import Club


class Schedule(BaseModel):

    DAY_MONDAY, DAY_TUESDAY, DAY_WEDNESDAY, DAY_THURSDAY, DAY_FRIDAY, DAY_SATURDAY, DAY_SUNDAY = range(7)

    DAY_CHOICES = (
        (DAY_MONDAY, _(u'Monday')),
        (DAY_TUESDAY, _(u'Tuesday')),
        (DAY_WEDNESDAY, _(u'Wednesday')),
        (DAY_THURSDAY, _(u'Thursday')),
        (DAY_FRIDAY, _(u'Friday')),
        (DAY_SATURDAY, _(u'Saturday'),),
        (DAY_SUNDAY, _(u'Sunday'))
    )

    club = models.ForeignKey(Club, related_name='schedule', verbose_name=_('club'), null=True)
    day = models.PositiveIntegerField(_('day'), choices=DAY_CHOICES)
    start_time = models.TimeField(_('start time'))
    end_time = models.TimeField(_('end time'))

    def __str__(self):
        return self.get_day_display()
