from django.contrib import admin

# Register your models here.
 
from app_01.models import Logger

@admin.register(Logger)
class LoggerAdmin(admin.ModelAdmin):
    readonly_fields = ('date_time',)
    fields = ('message', 'date_time', 'severity')
    list_display = ('message', 'date_time', 'severity')
    list_filter = ('severity',)

