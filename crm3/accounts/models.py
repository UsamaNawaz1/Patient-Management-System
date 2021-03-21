from django.db import models

# Create your models here.
class CreatePatient(models.Model):
	STATUS=(
			('Male','Male'),
			('Female','Female'),
			)
	BLOOD=(
			('A+','A+'),
			('A-','A-'),
			('B+','B+'),
			('B-','B-'),
			('O+','O+'),
			('O-','O-'),
			('AB+','AB+'),
			('AB-','AB-'),
			)
	first_name=models.CharField(max_length=200,null=True,)
	last_name=models.CharField(max_length=200,null=True)
	email=models.CharField(max_length=200,null=True)
	address=models.CharField(max_length=200,null=True)
	phone=models.CharField(max_length=200,null=True)
	gender=models.CharField(max_length=200,null=True,choices=STATUS)
	age=models.IntegerField(null=True)
	height=models.CharField(max_length=200,null=True)
	weight=models.CharField(max_length=200,null=True)
	blood_group=models.CharField(max_length=200,null=True,choices=BLOOD)

	def __str__(self):
		return self.first_name

class Prescription(models.Model):
	patient=models.ForeignKey(CreatePatient, null=True, on_delete=models.SET_NULL)
	medicines=models.CharField(max_length=200,null=True,)
	symptoms=models.CharField(max_length=200,null=True,)
	test=models.CharField(max_length=200,null=True,)
	diagnosis=models.CharField(max_length=200,null=True,)

	def __str__(self):
		return self.patient.first_name


class Medication(models.Model):
	name=models.CharField(max_length=200,null=True,)
	quantity=models.IntegerField(null=True)
	date_created=models.DateTimeField(auto_now_add=True,null=True)

	def __str__(self):
		return self.name