from django.db import models

class Merit(models.Model):
	session       = models.CharField(max_length=20)
	level  		  = models.CharField(max_length=20)
	student_name  = models.CharField(max_length=100)
	cgpa 		  = models.FloatField()
	position  	  = models.PositiveIntegerField()



class Teacher(models.Model):

	Apositive ='A+'
	Anegative ='A-'
	Bpositive ='B+'
	Bnegative ='B-'
	ABpositive ='AB+'
	ABegative ='AB-'
	Opositive ='O+'
	Onegative ='O-'
	blood_group='select from below'

	Lecturer ='Lecturer'
	Assi_Professor ='Assistant Professor'
	Asso_Professor='Associate Professor'
	Professor ='Professor'



	designation_choice =(
		(Lecturer,'Lecturer'),
		(Assi_Professor,'Assi_Professor'),
		(Asso_Professor,'Asso_Professor'),
		(Professor,'Professor'),

		)


	blood_group_choice =(

		(Apositive,'A+'),
		(Anegative,'A-'),
		(Bpositive,'B+'),
		(Bnegative,'B-'),
		(ABpositive,'AB+'),
		(ABegative,'AB-'),
		(Opositive,'O+'),
		(Onegative,'O-'),
		(blood_group,'select from below'),

		)
	teacher_name 	= 	models.CharField(max_length=100)
	designation		=	models.CharField(
					        max_length=20,
					        choices=designation_choice,
					        default=Lecturer,)
	address			=	models.CharField(max_length=300)
	contact_number	=	models.CharField(max_length=50)
	email			=	models.EmailField()
	blood_group		=	models.CharField(
					        max_length=20,
					        choices=blood_group_choice,
					        default=blood_group,)
	photo			=	models.ImageField(upload_to="CSE_BRUR/static/images/study/teacher")
	
class Student(models.Model):
	Apositive ='A+'
	Anegative ='A-'
	Bpositive ='B+'
	Bnegative ='B-'
	ABpositive ='AB+'
	ABegative ='AB-'
	Opositive ='O+'
	Onegative ='O-'
	blood_group_choice =(

		(Apositive,'A+'),
		(Anegative,'A-'),
		(Bpositive,'B+'),
		(Bnegative,'B-'),
		(ABpositive,'AB+'),
		(ABegative,'AB-'),
		(Opositive,'O+'),
		(Onegative,'O-'),

		)


	student_name 	= 	models.CharField(max_length=100)
	id_no           =   models.CharField(max_length=20)
	reg_no          =   models.CharField(max_length=20)
	batch           =   models.PositiveIntegerField()
	height_inch     =   models.FloatField()
	weight_kg       =   models.FloatField()
	contact_number	=	models.CharField(max_length=50)
	date_of_birth   =   models.DateField()
	address			=	models.CharField(max_length=300)
	email			=	models.EmailField()
	blood_group		=	models.CharField(
					        max_length=20,
					        choices=blood_group_choice,
					        default=Apositive,)
	photo			=	models.ImageField(upload_to="CSE_BRUR/static/images/study/student")
	
	