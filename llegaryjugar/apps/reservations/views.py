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

# Esto no es necesario
FORMS = [("Recintos", llegaryjugar.apps.reservations.forms.ClubForm),
        ("Horarios", llegaryjugar.apps.reservations.forms.ScheduleForm),
        ("Accesorios", llegaryjugar.apps.reservations.forms.AccesorieForm),
        ("Metodo", llegaryjugar.apps.reservations.forms.PaymentForm)]

# Esto tampoco
TEMPLATES = {"Recintos": "recintos.html",
            "Horarios": "horarios.html",
            "Accesorios": "accesorios.html",
            "Metodo": "metodo_pago.html"}

# Cambia el nombre a la clase porfa.
class ContactWizard(SessionWizardView):
        # template_name = 'template.html'  # Lo que te puse ayer
        # form_list = [ContactForm1, ContactForm2]  # Acá puedes definir los formularios, lo prefiero así por tema de que todo este en el mismo lugar

    # No lo veo necesario
    def get_template_names(self):
        return [TEMPLATES[self.steps.current]]

    def done(self, form_list, **kwargs):
        '''
        Acá solamente es el guardado Model.objects.create(**kwargs)
        y la respuesta, posiblemente un return reverse('url')
        '''
        return render_to_response('done.html', {
            'form_data': [form.cleaned_data for form in form_list],
        })
    def get_form_initial(self, step):
        # Acá es el valor inicial por ejemplo que el campo nombre ya venga con un nombre por defecto
        
        # steps are named 'step1', 'step2', 'step3'
        current_step = self.storage.current_step
        
        # get the data for step 1 on step 3
        if current_step == 'ContactForm2':
            prev_data = self.storage.get_step_data('ContactForm1')
            some_var = prev_data.get('ContactForm1-some_var','')
        
            return self.initial_dict.get(step, {'some_var': some_var})

        return self.initial_dict.get(step, {})
