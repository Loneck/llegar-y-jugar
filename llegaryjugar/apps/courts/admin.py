from django.contrib import admin

from llegaryjugar.apps.base.admin import BaseAdmin

from .models import Court, ScheduleCourt


@admin.register(Court)
class CourtAdmin(BaseAdmin):
    pass
    # filter_horizontal = ('schedules',)


@admin.register(ScheduleCourt)
class ScheduleCourtAdmin(BaseAdmin):
    pass
