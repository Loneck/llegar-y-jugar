from django.contrib import admin

from .models import Recinto, Cancha,Horario, Reserva


class RecintoAdmin(admin.ModelAdmin):
    list_display = ('nombre','latitud','longitud','id')
    search_fields = ('nombre',)


admin.site.register(Recinto,RecintoAdmin)
admin.site.register(Cancha)
admin.site.register(Horario)
admin.site.register(Reserva)
