from django.db import models

class donor_table(models.Model):
    phoneno = models.IntegerField(blank=True, null=True)
    unitno=models.CharField(max_length=10)

class patient_table(models.Model):
    unitno=models.CharField(max_length=10)
    uid = models.IntegerField(blank=True, null=True)
    name = models.CharField(max_length=10)