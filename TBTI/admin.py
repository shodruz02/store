from django.contrib import admin
from .models import TBTI

# Register your models here.

@admin.register(TBTI)
class TBTIAdmin(admin.ModelAdmin):
    list_display = ["name","address","Phone_number","Email","day_of_barth"]
    list_filter=["name","Phone_number"]
