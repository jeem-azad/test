from django.contrib import admin
from .models import Inovation
class inovationlist(admin.ModelAdmin):
	list_display = ['inovation_type','id_no','supervisor_name']

admin.site.register(Inovation,inovationlist)
