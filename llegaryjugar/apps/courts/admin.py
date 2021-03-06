from django.contrib import admin

from llegaryjugar.apps.base.admin import BaseAdmin

from .models import Court, ScheduleCourt


@admin.register(Court)
class CourtAdmin(BaseAdmin):
    pass
    list_display = ('club','name', 'is_active')
    # filter_horizontal = ('schedules',)


@admin.register(ScheduleCourt)
class ScheduleCourtAdmin(BaseAdmin):
    pass
    list_display = ('court', 'schedule', 'price')

