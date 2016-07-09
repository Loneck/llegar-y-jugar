from django.contrib import admin

from llegaryjugar.apps.base.admin import BaseAdmin

from .models import Reservations

@admin.register(Reservations)
class ReservationAdmin(BaseAdmin):
    pass
    list_display = ('author', 'club', 'schedule', 'reserved_at', 'accesorie', 'price')