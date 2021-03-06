from django.contrib import admin

from llegaryjugar.apps.base.admin import BaseAdmin

from .models import Schedule


@admin.register(Schedule)
class ScheduleAdmin(BaseAdmin):
    pass
    list_display = ('club', 'date', 'day', 'start_time', 'end_time')
    