from django.contrib import admin
from .models import Blog


@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ('name',)
    list_filter = ('name', 'description', 'watch_count')
    search_fields = ('name', 'watch_count',)
