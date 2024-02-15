from django.contrib import admin
from .models import Providers

# Register your models here.

@admin.register(Providers)
class ProvidersAdmin(admin.ModelAdmin):
    list_display = ["name","address","Phone_number","Email"]
    list_filter=["name","Phone_number"]
