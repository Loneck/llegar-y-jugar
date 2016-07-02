# -*- coding: utf-8 -*-
from django.template import RequestContext
from django.shortcuts import render_to_response, render
from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate, login
from formtools.wizard.views import SessionWizardView
from django.core.mail import send_mail
from django.template.response import TemplateResponse
from llegaryjugar.apps.reservations.forms import ClubForm, ScheduleForm, AccesorieForm, PaymentForm
from llegaryjugar.apps.reservations.models import Reservations

# def club_list(request):
#     clubs = Club.objects.all()
#     return render(request, 'inicio/inicio.html', {'clubs': clubs})

class StepWizard(SessionWizardView):
    template_name = 'wizard_form.html'
    form_list = [ClubForm, ScheduleForm, AccesorieForm, PaymentForm] 


    def done(self, form_list, form_dict, **kwargs):
        # data = {k: v for form in form_list for k, v in form.cleaned_data.items()}
        # instance = Reservations()

        # for form in form_list:
        #     for key, value in form.cleaned_data.iteritems():
        #         setattr(instance, key, value)
        #     instance.save()
        # print form_list
        # print form_dict
        # reserve = Reservations(**form_dict)
        
        reserve = Reservations.objects.create(club = form_dict['0'], schedule = form_dict['1'], accesorie = form_dict['2'], price = form_dict['3'])
        # reserve = Reservations(schedule = 'club')
        # reserve.save()

        return render_to_response('done.html', {
            'form_data': [form.cleaned_data for form in form_list],
            })

    def get_form_initial(self, step):
        # Acá es el valor inicial por ejemplo que el campo nombre ya venga con un nombre por defecto
                
        # steps are named 'step1', 'step2', 'step3'
        current_step = self.storage.current_step
                
        # get the data for step 1 on step 3
        if current_step == 'ScheduleForm':
            prev_data = self.storage.get_step_data('ClubForm')
            some_var = prev_data.get('ClubForm-some_var','')
                
            return self.initial_dict.get(step, {'some_var': some_var})

        return self.initial_dict.get(step, {})
