from django.db import models

class Donation(models.Model):
	donation_method       = models.CharField(max_length=100)
	procedure             = models.TextField()
	contact_number        = models.CharField(max_length=50)
	
class Helpline(models.Model):
	description           = models.TextField()
	purpose               = models.CharField(max_length=100)
	contact_number        = models.CharField(max_length=50)

class Blood_bank(models.Model):
	doner_name            = models.CharField(max_length=100)
	blood_group           = models.CharField(max_length=100)
	contact_number        = models.CharField(max_length=50)
	donation_date         = models.DateTimeField()
	description           = models.TextField()
	