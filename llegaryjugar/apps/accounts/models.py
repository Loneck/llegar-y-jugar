from __future__ import unicode_literals
from django.db import models
from django.dispatch import receiver
from django.db.models.signals import post_save
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.models import User
from django.contrib.auth import login
from django.template.defaultfilters import slugify
from django.core.urlresolvers import reverse
from django.core.validators import MaxLengthValidator

class Profile(models.Model):
    user = models.ForeignKey('auth.User', related_name='profile')
    user_slug = models.SlugField(_('Slug'), editable=False, null=True)
    photo = models.ImageField(_('Photo'), blank=True, upload_to='accounts/profile/avatar', null=True)
    location = models.CharField(_('Location'), max_length=140, blank=True)
    about = models.TextField(_('About'), blank=True, validators=[MaxLengthValidator(150)], help_text=_('Maximum 150 Characters'))

    def get_absolute_url(self):
        return reverse('accounts.views.author_view_detail', kwargs={'slug': self.user_slug})

    def __str__(self):
        return self.user.username
