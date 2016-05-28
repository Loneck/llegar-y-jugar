from __future__ import unicode_literals

from django.db import models
from django.utils.translation import ugettext as _

from llegaryjugar.apps.base.models import BaseModel
from ajaximage.fields import AjaxImageField


class ClubManager(models.Manager):
    use_for_related_fields = True

    def active(self):
        return self.get_queryset().filter(is_active=True)


class Club(BaseModel):
    name = models.CharField(_('name'), max_length=50)
    address = models.CharField(_('address'), max_length=50)
    description = models.TextField(_('description'))
    logo = AjaxImageField(_('image'), upload_to='clubs/logo/')
    is_active = models.BooleanField(_('is active'), default=True)

    objects = ClubManager()

    def __str__(self):
        return self.name
