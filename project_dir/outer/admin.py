from django.contrib import admin

from .models import Request_JSONB


class JSONB_Admin(admin.ModelAdmin):
    list_display = ('timestamp','request_set')
    list_display_links = ('request_set',)

admin.site.register(Request_JSONB,JSONB_Admin)