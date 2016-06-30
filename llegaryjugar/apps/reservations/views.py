# -*- coding: utf-8 -*-
from django.template import RequestContext
from django.shortcuts import render_to_response, render
from llegaryjugar.forms import LoginForm
from django.contrib.auth import authenticate, login
from formtools.wizard.views import SessionWizardView
from django.core.mail import send_mail
from django.template.response import TemplateResponse
from llegaryjugar.apps.reservations.models import Club

# class StepWizard(SessionWizardView):
#   template_name = "inicio.html"

#   def done(self, form_list, **kwargs):
#       form_data = process_form_data(form_list)

#       return render_to_response('done.html', {'form_data': form_data})

#   def process_form_data(form_list):
#       form_data = [form.cleaned_data for form in form_list]

#       logr.debug(form_data[0]['club'])
#       logr.debug(form_data[1]['scheduleCourt'])
#       logr.debug(form_data[2]['accesories'])
#       logr.debug(form_data[3]['paymentMethod'])

#       send_mail(form_data[0]['club'],
#                 form_data[1]['scheduleCourt'],
#                 form_data[2]['accesories'],
#                 form_data[3]['paymentMethod'],
#                 ['leo.torrejon@gmail.com'], fail_silently=False)

#       return form_data

#   def get_form_initial(self, step):
#       return self.initial_dict.get(step, {'hola': 1234})


def club_list(request):
    clubs = Club.objects.all()
    return render(request, 'inicio/inicio.html', {'clubs': clubs})


class ContactWizard(SessionWizardView):
    template_name = 'wizard_form.html'

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
