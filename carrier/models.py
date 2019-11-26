from django.db import models


# Create your models here.
class Carrier(models.Model):
	topic = models.CharField(max_length=100)
	description  = models.TextField()
	scope        = models.CharField(max_length=300)
	ref_link     = models.URLField()