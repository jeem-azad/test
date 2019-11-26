from django.contrib import admin
from .models import Image, Archive, Events, Cse_club, Game_achivement, Player 

class imagelist(admin.ModelAdmin):

	list_display =['image_category']

class archivelist(admin.ModelAdmin):
	list_display =['archive_category']

class eventlist(admin.ModelAdmin):

	list_display =['event_name']

class cse_clublist(admin.ModelAdmin):
	list_display =['club_member']


class game_achivementlist(admin.ModelAdmin):
	list_display =['achivement_title']

class playerlist(admin.ModelAdmin):
	list_display =['player_name']

admin.site.register(Image,imagelist)
admin.site.register(Archive,archivelist)
admin.site.register(Events,eventlist)
admin.site.register(Cse_club,cse_clublist)
admin.site.register(Game_achivement,game_achivementlist)
admin.site.register(Player,playerlist)