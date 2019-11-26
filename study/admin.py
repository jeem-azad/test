from django.contrib import admin
from .models import Merit,Teacher,Student


class meritlist(admin.ModelAdmin):
	list_display = ['session','student_name']
class Tracherlist(admin.ModelAdmin):
	list_display = ['teacher_name','designation','contact_number']

class Studentlist(admin.ModelAdmin):
	list_display = ['student_name','id_no','batch']

admin.site.register(Merit,meritlist)
admin.site.register(Teacher,Tracherlist)
admin.site.register(Student,Studentlist)
