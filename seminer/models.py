from django.db import models

class Inovation (models.Model):
	Thesis ="Thesis"
	Project ="Project"
	Extar ="other inovation"
	inovation_choice = (
		(Thesis,'Thesis'),
		(Project,'Project'),
		(Extar,'other inovation')

		)
	inovation_type        = models.CharField(
					        max_length=20,
					        choices=inovation_choice,
					        default=Thesis,)
	inovation_title       = models.CharField(max_length=100)
	inovation_description =	models.TextField()
	id_no                 = models.CharField(max_length=20)
	supervisor_name       = models.CharField(max_length=100)
	rating 				  = models.PositiveIntegerField()
	publication 		  =	models.URLField()


