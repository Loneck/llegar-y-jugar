from django import forms

from django.db import models
from django.contrib import admin
from django.utils.translation import ugettext as _

from llegaryjugar.apps.clubs.models import Club
from llegaryjugar.apps.courts.models import ScheduleCourt
from llegaryjugar.apps.reservations.models  import Reservations
from llegaryjugar.apps.accesorie.models import Accesorie

# class StepForm1(forms.Form):
#     club = models.ForeignKey(Club, related_name='court', verbose_name=_('club'))

# class StepForm2(forms.Form):
#     scheduleCourt = models.ForeignKey(Schedule, related_name='schedule_courtyard', verbose_name=_('schedule'))

# class StepForm3(forms.Form):
#     message = forms.CharField(max_length=100)

# class StepForm4(forms.Form):
#     message = forms.CharField(max_length=100)


class ClubForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        self.club = kwargs.pop('club', None)
        super(ClubForm, self).__init__(*args, **kwargs)

    class Meta:
        model = Reservations
        fields = ('club',)


class ScheduleForm(ClubForm):

    def __init__(self, *args, **kwargs):
        super(ScheduleForm, self).__init__(*args, **kwargs)
        self.fields['schedule'].queryset = ScheduleCourt.objects.filter(court__club=self.club)

    class Meta(ClubForm.Meta):
        fields = ('schedule',)


class AccesorieForm(ClubForm):

    def __init__(self, *args, **kwargs):
        super(AccesorieForm, self).__init__(*args, **kwargs)
        self.fields['accesorie'].queryset = Accesorie.objects.filter(club=self.club)

    class Meta(ClubForm.Meta):
        fields = ('accesorie',)


class PaymentForm(ClubForm):

    def __init__(self, *args, **kwargs):
        super(PaymentForm, self).__init__(*args, **kwargs)
        # self.fields['price'].queryset = ScheduleCourt.objects.filter(price=self.price)

    class Meta(ClubForm.Meta):
        fields = ('price',)
