# -*- coding: utf-8 -*-
from django.shortcuts import render

from django.views.generic import ListView, DetailView
from django.views.generic.edit import UpdateView
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from django.core.urlresolvers import reverse
from django.contrib import messages
from django.utils.translation import ugettext as _

from registration.backends.default.views import RegistrationView
from registration.forms import RegistrationFormUniqueEmail

from .models import Profile
from .forms import ProfileForm


class ProfileDetail(DetailView):
    model = Profile

    @method_decorator(login_required)
    def dispatch(self, request):
        return super(ProfileDetail, self).dispatch(request=request)

    def get_object(self, queryset=None):
        profile, self.created = Profile.objects.get_or_create(user=self.request.user)
        return profile

profile_detail_view = ProfileDetail.as_view()


class ProfileEditView(UpdateView):
    model = Profile
    form_class = ProfileForm

    @method_decorator(login_required)
    def dispatch(self, request):
        return super(ProfileEditView, self).dispatch(request=request)

    def get_object(self, queryset=None):
        profile, self.created = Profile.objects.get_or_create(user=self.request.user)
        return profile

    def get_success_url(self, instance=None):
        messages.success(self.request, _(u'Sus Datos Se Han Actualizado Con Éxito'))
        return reverse('accounts.views.profile_edit_view')

profile_edit_view = ProfileEditView.as_view()