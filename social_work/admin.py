from django.contrib import admin
from .models import Donation, Blood_bank,Helpline



class Donationlist(admin.ModelAdmin):

	list_display =['donation_method']

class Blood_banklist(admin.ModelAdmin):

	list_display =['doner_name']

class Helplinelist(admin.ModelAdmin):

	list_display =['purpose']

admin.site.register(Blood_bank,Blood_banklist)
admin.site.register(Donation,Donationlist)
admin.site.register(Helpline,Helplinelist)
