from django.contrib import admin

# Register your models here.
from .models import *

admin.site.register(CreatePatient)
admin.site.register(Prescription)
admin.site.register(Medication)