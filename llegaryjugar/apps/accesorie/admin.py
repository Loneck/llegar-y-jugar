from django.contrib import admin
from llegaryjugar.apps.base.admin import BaseAdmin
from .models import Accesorie

@admin.register(Accesorie)
class AccesorieAdmin(BaseAdmin):
    pass
    list_display = ('name', 'club', 'price', 'is_active')