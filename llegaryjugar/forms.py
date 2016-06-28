from django import forms

from django.contrib import admin
from django.utils.translation import ugettext as _

class LoginForm(forms.Form):
	username = forms.CharField()
	password = forms.CharField(widget = forms.PasswordInput())