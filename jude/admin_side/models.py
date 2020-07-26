from django.db import models


class Donor(models.Model):
    phoneno = models.BigIntegerField()
    unitno = models.IntegerField()


class Center(models.Model):
    center_name = models.CharField(max_length=50, primary_key=True)
    center_location = models.CharField(max_length=50)


class Patients(models.Model):
    uid = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=30)
    unitno = models.IntegerField()
    prefered_language = models.CharField(max_length=30)
    checkin_date_time = models.DateTimeField()
    discharged_date_time = models.DateTimeField()
    center_name = models.CharField(max_length=50)
    contact_number = models.BigIntegerField()


class Language(models.Model):
    language_id = models.IntegerField(primary_key = True)
    language_name = models.CharField(max_length=15)


class Questions(models.Model):
    question_id = models.IntegerField(primary_key = True)
    question = models.TextField(max_length=250)
    language_id = models.ForeignKey(Language, on_delete=models.CASCADE)


class PatientFeedback(models.Model):
    uid = models.IntegerField()
    question_id = models.ForeignKey(Questions, on_delete=models.CASCADE)
    rating = models.IntegerField()
