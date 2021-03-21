from django.urls import path
from . import views

urlpatterns=[
	
	path('',views.LoginPage,name='login'),
	path('Dashboard/',views.Home,name='home'),
	path('Doctors/',views.Doctors,name='doctors'),
	path('Patients/',views.Patients,name='patients'),
	path('Profile/<str:pk>/',views.ProfilePatient,name='profile'),
	path('AddPatient/',views.Add_Patient,name='add_patients'),
	path('Patient/<str:pk>/',views.UpdateSinglepatient,name='single_patient'),
	path('Patient/Delete/<str:pk>/',views.DeleteSinglepatient,name='delete_patient'),
	path('displayprescriptions/',views.Printprescriptions,name='display_prescriptions'),
	path('printprescriptions/<str:pk>/',views.ProfilePrescription,name='print_prescription'),
	path('prescription/',views.AddPrescription,name='prescription'),
	path('Prescription/<str:pk>/',views.UpdatePrescription,name='update_prescription'),
	path('Prescription/Delete/<str:pk>/',views.Deleteprescription,name='delete_prescription'),
	path('AddMedicine/',views.Add_Medicines,name='add_medicine'),
	path('printMedicine/',views.print_medication,name='print_medication'),
	path('Medicines/<str:pk>/',views.Deletemedication,name='delete_medicine'),
	path('Login/',views.LoginPage,name='login'),
	path('Register/',views.RegisterPage,name='register'),
	path('logout/',views.logoutUser,name='logout')
]
