# -*- coding: utf-8 -*-
from django.template import RequestContext
from django.shortcuts import render_to_response, render
from django.http import HttpResponseRedirect
from django.contrib.auth import authenticate, login
from django.core.mail import send_mail
from django.template.response import TemplateResponse
from django.shortcuts import redirect

from formtools.wizard.views import SessionWizardView

from llegaryjugar.apps.reservations.forms import ClubForm, ScheduleForm, AccesorieForm, PaymentForm
from llegaryjugar.apps.reservations.models import Reservations

# def club_list(request):
#     clubs = Club.objects.all()
#     return render(request, 'inicio/inicio.html', {'clubs': clubs})


class StepWizard(SessionWizardView):
    template_name = 'wizard_form.html'
    form_list = [ClubForm, ScheduleForm, AccesorieForm, PaymentForm]
    instance = None

    def get_form_kwargs(self, step=None):
        kwargs = {}
        if step == '1' or step == '2':
            club = self.get_cleaned_data_for_step('0')['club']
            kwargs.update(
                {'club': club}
            )
        return kwargs

    def get_context_data(self, form, **kwargs):
        context = super(StepWizard, self).get_context_data(form=form, **kwargs)
        if self.steps.current == '3':
            schedule = self.get_cleaned_data_for_step('1')['schedule']
            self.price = schedule.price
            context.update({'price': self.price})
        return context

    def get_form_instance(self, step):
        if self.instance is None:
            self.instance = Reservations()
        return self.instance

    def get_form_initial(self, step):
        initial_dict = {}
        if self.steps.current == '3':
            #algoQueLeDigaDeDondeSacarPrice
            initial_dict = { 'price': self.price }
        return initial_dict

    # def get_form_initial(self, step):
    #     return self.initial_dict.get(step, {'price': self.price})

    def done(self, form_list, **kwargs):

        data = {}
        for form in form_list:
            data.update(form.cleaned_data)
        Reservations.objects.create(**data)

        return redirect('/')

    # def done(self, form_list, form_dict, **kwargs):
    #     # data = {k: v for form in form_list for k, v in form.cleaned_data.items()}
    #     # instance = Reservations()

    #     # for form in form_list:
    #     #     for key, value in form.cleaned_data.iteritems():
    #     #         setattr(instance, key, value)
    #     #     instance.save()
    #     print form_list
    #     print form_dict

    #     # data = {}
    #     # for form in form_list:
    #     #     for k,v in form.__dict__.items():
    #     #         data[k] = v if v else data.get(k)

    #     # # Save it to the first form
    #     # form_list[0].__dict__.update(data)
    #     # form_list[0].save()
    #     # reserve = Reservations(**form_dict)
    #     # reserve = Reservations.objects    .create(club = form_dict['ClubForm'], schedule = form_dict['ClubForm'], accesorie = form_dict['ClubForm'], price = form_dict['ClubForm'])
    #     # reserve = Reservations(club = 'club', schedule = 'schedule',**form_dict)
    #     # reserve.save()

    #     return render_to_response('done.html', {
    #         'form_data': [form.cleaned_data for form in form_list],
    #         })
