from django.forms import ModelForm
from .models import CreatePatient,Prescription,Medication
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.auth.models import User



class CreatePatientForm(ModelForm):
	class Meta:
		model=CreatePatient
		fields='__all__'

class CreatePrescriptionForm(ModelForm):
	class Meta:
		model=Prescription
		fields='__all__'

class CreateUserForm(UserCreationForm):
	class Meta:
		model = User
		fields = ['username','first_name', 'email', 'password1', 'password2']


class MedicationForm(ModelForm):
	class Meta:
		model=Medication
		fields=['name','quantity']