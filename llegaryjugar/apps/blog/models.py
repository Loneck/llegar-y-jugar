from __future__ import unicode_literals
from django.db import models
from django.utils import timezone
from django.contrib import admin
from django.utils.translation import ugettext as _
from llegaryjugar.apps.base.models import BaseModel
from llegaryjugar.apps.clubs.models import Club
from ajaximage.fields import AjaxImageField

class  Post(models.Model):
	author = models.ForeignKey('auth.User')
	title = models.CharField(max_length=200)
	text = models.TextField()
	logo = AjaxImageField(_('image'), upload_to='blog/image/', null=True)
	created_at = models.DateTimeField(
		default=timezone.now)
	published_date = models.DateTimeField(
		blank=True, null=True)
	is_active = models.BooleanField(_('is active'), default=True)

	def publish(self):
		self.published_date = timezone.now()
		self.save()

	def __str__(self):
		return self.title