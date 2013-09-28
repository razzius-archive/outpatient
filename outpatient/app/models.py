from django.db import models

# Create your models here.

class Doctor(models.Model):
    name = models.CharField(max_length=50)
    address = models.CharField(max_length=128)
    postal_code = models.CharField(max_length=20)
    city = models.CharField(max_length=80)
    state = models.CharField(max_length=80)

class Reminder(models.Model):
    doctor = models.ForeignKey(Doctor)
    recipient = models.CharField(max_length=80) # phone #
    msg = models.CharField(max_length=140)
    scheduled_time = models.DateTimeField()
