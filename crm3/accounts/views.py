from django.shortcuts import render,redirect
from django.http import HttpResponse
# Create your views here.
from .forms import  CreateUserForm,CreatePatientForm,CreatePrescriptionForm,MedicationForm
from .models import *
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.forms import inlineformset_factory
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout

from django.contrib import messages
from django.contrib.auth.models import Group
from .decorators import unauthenticated_user, allowed_users, admin_only



@allowed_users(allowed_roles=['Doctors','Nurses'])
def Home(request):
	patients=CreatePatient.objects.all()
	doctors=User.objects.all()
	medications=Medication.objects.all()
	total_patients=patients.count()
	total_doctors=doctors.count()
	total_medications=medications.count()
	context={
			'patients':patients,
			'total_patients':total_patients,
			'doctors':doctors,
			'total_doctors':total_doctors,
			'total_medications':total_medications

	}
	return render(request,'accounts/index.html',context)

def Doctors(request):
	doctors=User.objects.all()
	context={
			'doctors':doctors
	}
	return render(request, 'accounts/doctors.html',context)

def Patients(request):
	patients=CreatePatient.objects.all()
	context={
			'patients':patients
	}
	return render(request, 'accounts/patients.html',context)

def Printprescriptions(request):
	prescriptions=Prescription.objects.all()
	context={
			'prescriptions':prescriptions
	}
	return render(request, 'accounts/display_prescriptions.html',context)








@allowed_users(allowed_roles=['Doctors'])
def UpdateSinglepatient(request,pk):
	patient = CreatePatient.objects.get(id=pk)
	form = CreatePatientForm(instance=patient)

	if request.method == 'POST':
		form = CreatePatientForm(request.POST, instance=patient)
		if form.is_valid():
			form.save()
			return redirect('/')

	context = {'form':form}
	return render(request,'accounts/add-patient.html',context)


@allowed_users(allowed_roles=['Doctors'])
def DeleteSinglepatient(request,pk):
	patient = CreatePatient.objects.get(id=pk)
	patient.delete()
	return redirect('patients')

	

@allowed_users(allowed_roles=['Doctors'])
def UpdatePrescription(request,pk):
	prescription = Prescription.objects.get(id=pk)
	form = CreatePrescriptionForm(instance=prescription)

	if request.method == 'POST':
		form = CreatePrescriptionForm(request.POST, instance=prescription)
		if form.is_valid():
			form.save()
			return redirect('/')

	context = {'form':form}
	return render(request,'accounts/prescriptions.html',context)

@allowed_users(allowed_roles=['Doctors'])
def Deleteprescription(request,pk):
	prescription = Prescription.objects.get(id=pk)
	prescription.delete()
	return redirect('display_prescriptions')


def ProfilePrescription(request,pk):
	pres = Prescription.objects.get(id=pk)
	
	context={
		'pres':pres,
	}
	return render(request,'accounts/pres.html',context)


def ProfilePatient(request,pk):
	pat = CreatePatient.objects.get(id=pk)
	
	context={
		'pat':pat,
	}
	return render(request,'accounts/profile.html',context)

@allowed_users(allowed_roles=['Doctors'])
def AddPrescription(request):
	
	form=CreatePrescriptionForm()
	if request.method=='POST':
		form=CreatePrescriptionForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('/')
	context={'form':form}
	return render(request,'accounts/prescriptions.html',context)
	
@allowed_users(allowed_roles=['Doctors'])
def Add_Patient(request):
	form=CreatePatientForm()
	if request.method=='POST':
		form=CreatePatientForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('/')
	context={'form':form}
	return render(request,'accounts/add-patient.html',context)



def Add_Medicines(request):
	form=MedicationForm()
	if request.method=='POST':
		form=MedicationForm(request.POST)
		if form.is_valid():
			form.save()
			return redirect('/')
	context={'form':form}
	return render(request,'accounts/medication.html',context)


def print_medication(request):
	medications=Medication.objects.all()
	context={
			'medications':medications,
	}
	return render(request,'accounts/display_medication.html',context)

def Deletemedication(request,pk):
	medications = Medication.objects.get(id=pk)
	medications.delete()
	return redirect('print_medication')

@unauthenticated_user
def LoginPage(request):
	if request.method=='POST':
			username=request.POST.get('username')
			password=request.POST.get('password')
			user=authenticate(request, username=username, password=password)
			if user is not None:
				login(request, user)
				return redirect('home')
			else:
				messages.info(request, 'Username or Password is incorrect')
	return render(request, 'accounts/login.html')

@unauthenticated_user
def RegisterPage(request):

	form=CreateUserForm()

	if request.method=='POST':
		form=CreateUserForm(request.POST)
		if form.is_valid():
			user=form.save()
			username=form.cleaned_data.get('username')
			role=form.cleaned_data.get('first_name')
			if role == 'Doctor':
				group = Group.objects.get(name='Doctors')
				user.groups.add(group)
			elif role == 'Nurse':
				group = Group.objects.get(name='Nurses')
				user.groups.add(group)
			messages.success(request, 'Account is created for '+username)
			return redirect('login')
	context={'form':form}
	return render(request,'accounts/register.html',context)
	

def logoutUser(request):
	logout(request)
	return redirect('login')