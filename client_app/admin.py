from django.contrib import admin
from .models import Client

# Register your models here.
class ClientAdmin(admin.ModelAdmin):
    list_display = ('client_name', 'client_email')
admin.site.register(Client, ClientAdmin)
