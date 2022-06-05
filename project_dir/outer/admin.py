from django.contrib import admin

from .models import Request_JSONB_Model


class JSONB_Admin(admin.ModelAdmin):
    list_display = ('timestamp',)
    list_display_links = ('timestamp',)

admin.site.register(Request_JSONB_Model,JSONB_Admin)