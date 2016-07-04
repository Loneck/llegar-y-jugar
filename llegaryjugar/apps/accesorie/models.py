from __future__ import unicode_literals

from django.db import models
from django.contrib import admin
from django.utils.translation import ugettext as _

from llegaryjugar.apps.base.models import BaseModel
from llegaryjugar.apps.clubs.models import Club

class Accesorie(BaseModel):
    club = models.ForeignKey(Club, related_name='accesorie', verbose_name=_('club'), null=True)
    name = models.CharField(_('name'), max_length=50)
    description = models.TextField(_('description'))
    price = models.DecimalField(_('price'), decimal_places=2, max_digits=30)
    is_active = models.BooleanField(_('is active'), default=True)

    def __str__(self):
        return '%s' %(self.name)