from django.db import models

class Image(models.Model):
	image_category       = models.CharField(max_length=100)
	description          = models.TextField()
	photo		         = models.ImageField(upload_to="CSE_BRUR/static/images/co_curricular/Image")
	like                 = models.IntegerField(default=0)


class Events(models.Model):
	event_name       = models.CharField(max_length=100)
	event_type       = models.CharField(max_length=100)
	event_date       = models.DateTimeField()
	description      = models.TextField()
	banner_photo	 = models.ImageField(upload_to="CSE_BRUR/static/images/co_curricular/Events")
	event_category   = models.CharField(max_length=100)
	event_schedule   = models.CharField(max_length=300)


class Archive(models.Model):
	session          =  models.CharField(max_length=20)
	archive_category =  models.CharField(max_length=100)
	photo		     =  models.ImageField(upload_to="CSE_BRUR/static/images/co_curricular/Archive")
	description      =	models.TextField()

class Cse_club(models.Model):
	club_member      = models.CharField(max_length=100)
	club_designation = models.CharField(max_length=100)
	photo 			 = models.ImageField(upload_to="CSE_BRUR/static/images/co_curricular/Cse_club")
	contact_number   = models.CharField(max_length=50)
	email 			 = models.EmailField()

class Game_achivement(models.Model):
	achivement_title       =  models.CharField(max_length=100)
	achivement_description =  models.TextField()
	photo		           =  models.ImageField(upload_to="CSE_BRUR/static/images/co_curricular/Game_achivement")

class Player(models.Model):
	player_name     = models.CharField(max_length=100)
	batch           = models.PositiveIntegerField()
	player_category = models.CharField(max_length=100)
	description     = models.TextField() 
	achivement      = models.CharField(max_length=100)
	



