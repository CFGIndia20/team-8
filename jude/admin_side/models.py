from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser):
    name = models.CharField(max_length=256)
    password = models.CharField(max_length=100)
    telephone = models.CharField(max_length=10)
    flat_no = models.CharField(max_length=20)
    email = models.EmailField(max_length=100)
    rights = models.CharField(max_length=10, default="Normal")


class Donor(models.Model):
    user_id = models.ForeignKey(CustomUser, on_delete=models.CASCADE)


class Center(models.Model):
    center_name = models.CharField(max_length=50)
    center_location = models.CharField(max_length=50)


class Unit(models.Model):
    donor_id = models.ForeignKey(Donor, on_delete=models.CASCADE)


class Patients(models.Model):
    uid = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=30)
    unitno = models.IntegerField()
    prefered_language = models.CharField(max_length=30)
    checkin_date_time = models.DateTimeField()
    discharged_date_time = models.DateTimeField()


class Family(models.Model):
    patient_id = models.ForeignKey(Patients, on_delete=models.CASCADE)
    contact_number = models.BigIntegerField()


class Language(models.Model):
    language_name = models.CharField(max_length=15)


class Questions(models.Model):
    question = models.TextField(max_length=250)
    language_id = models.ForeignKey(Language, on_delete=models.CASCADE)


class PatientFeedback(models.Model):
    patient_id = models.ForeignKey(Patients, on_delete=models.CASCADE)
    question_id = models.ForeignKey(Questions, on_delete=models.CASCADE)
