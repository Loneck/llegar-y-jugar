# -*- coding: utf-8 -*-
from django.template import RequestContext
from django.shortcuts import render_to_response
from llegaryjugar.forms import LoginForm
from django.contrib.auth import authenticate, login
from formtools.wizard.views import SessionWizardView
from django.core.mail import send_mail

def login_page(request):
	message = None
	if request.method == "POST":
		form = LoginForm(request.POST)
		if form.is_valid():
			username = request.POST['username']
			password = request.POST['password']
			user = authenticate(username=username, password=password)
			if user is not None:
				if user.is_active:
					login(request, user)
					message = "Has ingresado correctamente"
				else:
					message = "Tu usuario está desactivado"
			else:
				message = "Nombre de usuario y/o password incorrecto"
	else:
		form = LoginForm()
	return render_to_response('login.html', {'message': message, 'form': form}, context_instance = RequestContext(request))