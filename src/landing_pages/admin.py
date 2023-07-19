from django.contrib import admin

# Register your models here.
from .models import LnadingPageEntry

class LandingPageEntryAdmin(admin.ModelAdmin):
    list_display=["name","email"]
    search_fields=["name","email"]

admin.site.register(LnadingPageEntry,LandingPageEntryAdmin)
