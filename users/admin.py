from django.contrib import admin
from .models import CustomUser


@admin.register(CustomUser)
class CustomUserAdmin(admin.ModelAdmin):
    list_display = ('id', 'email', 'phone_num', 'token')
    list_filter = ('email', 'phone_num')
    search_fields = ('email', 'phone_num',)
