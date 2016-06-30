from django.contrib import admin
from llegaryjugar.apps.base.admin import BaseAdmin
from .models import Post

# Register your models here.
@admin.register(Post)
class BlogAdmin(BaseAdmin):
    pass
    list_display = ('title','author', 'created_at', 'is_active')