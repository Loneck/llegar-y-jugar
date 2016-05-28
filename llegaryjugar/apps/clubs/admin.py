from django.contrib import admin

from llegaryjugar.apps.base.admin import BaseAdmin

from .models import Club


@admin.register(Club)
class ClubAdmin(BaseAdmin):
    pass
