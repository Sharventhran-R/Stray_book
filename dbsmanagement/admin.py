from django.contrib import admin
from .models import Info
from .forms import InfoForm


class InfoAdmin(admin.ModelAdmin):
   list_display = ['number', 'animal', 'date']
   form = InfoForm
   list_filter = ['number', 'name', 'date']
   search_fields = ['number', 'name', 'date', 'animal']

admin.site.register(Info, InfoAdmin)
# Register your models here.
