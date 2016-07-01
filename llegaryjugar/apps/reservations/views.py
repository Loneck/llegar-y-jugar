# -*- coding: utf-8 -*-
from django.template import RequestContext
from django.shortcuts import render_to_response, render
from llegaryjugar.forms import LoginForm
from django.contrib.auth import authenticate, login
from formtools.wizard.views import SessionWizardView
from django.core.mail import send_mail
from django.template.response import TemplateResponse
from llegaryjugar.apps.reservations.models import Club
from llegaryjugar.apps.reservations.forms import ClubForm, ScheduleForm, AccesorieForm, PaymentForm

# def club_list(request):
#     clubs = Club.objects.all()
#     return render(request, 'inicio/inicio.html', {'clubs': clubs})


FORMS = [("Recintos", llegaryjugar.apps.reservations.forms.ClubForm),
        ("Horarios", llegaryjugar.apps.reservations.forms.ScheduleForm),
        ("Accesorios", llegaryjugar.apps.reservations.forms.AccesorieForm),
        ("Metodo", llegaryjugar.apps.reservations.forms.PaymentForm)]

TEMPLATES = {"Recintos": "recintos.html",
            "Horarios": "horarios.html",
            "Accesorios": "accesorios.html",
            "Metodo": "metodo_pago.html"}

class ContactWizard(SessionWizardView):
    def get_template_names(self):
        return [TEMPLATES[self.steps.current]]

    def done(self, form_list, **kwargs):
        return render_to_response('done.html', {
            'form_data': [form.cleaned_data for form in form_list],
        })
    def get_form_initial(self, step):

        # steps are named 'step1', 'step2', 'step3'
        current_step = self.storage.current_step
        
        # get the data for step 1 on step 3
        if current_step == 'ContactForm2':
            prev_data = self.storage.get_step_data('ContactForm1')
            some_var = prev_data.get('ContactForm1-some_var','')
        
            return self.initial_dict.get(step, {'some_var': some_var})

        return self.initial_dict.get(step, {})
