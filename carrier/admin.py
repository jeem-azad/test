from django.contrib import admin
from .models import Carrier 
# Register your models here.
class carrierlist(admin.ModelAdmin):
	list_display = ['topic','scope']

admin.site.register(Carrier,carrierlist)