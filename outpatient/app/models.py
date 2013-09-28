from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Doctor(models.Model):
    name = models.CharField(max_length=50)
    location = models.CharField(max_length=200)

class Reminder(models.Model):
    doctor = models.ForeignKey(Doctor)
    recipient = models.CharField(max_length=80) # phone #
    msg = models.CharField(max_length=140)
    scheduled_time = models.DateTimeField()
    sent24 = models.BooleanField()
    sent1 = models.BooleanField()
