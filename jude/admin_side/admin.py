from django.contrib import admin

# Register your models here.
from .models import Donor, Patients, PatientFeedback, Center, Questions, Language

admin.site.register(Donor)
admin.site.register(Patients)
admin.site.register(PatientFeedback)
admin.site.register(Center)
admin.site.register(Questions)
admin.site.register(Language)
