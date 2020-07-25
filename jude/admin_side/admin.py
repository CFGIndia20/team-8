from django.contrib import admin

# Register your models here.
from .models import Donor, Patients, PatientFeedback, Unit, Center, Questions, Language, Family,CustomUser

admin.site.register(Donor)
admin.site.register(Patients)
admin.site.register(PatientFeedback)
admin.site.register(Unit)
admin.site.register(Center)
admin.site.register(Questions)
admin.site.register(Language)
admin.site.register(Family)
admin.site.register(CustomUser)