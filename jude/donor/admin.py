from django.contrib import admin
from donor.models import donor_table, patient_table 

admin.site.register(donor_table)
admin.site.register(patient_table)