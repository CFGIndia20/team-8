from django.contrib import admin

# Register your models here.
from donor.models import donor_table, patient_table 

admin.site.register(donor_table)
admin.site.register(patient_table)