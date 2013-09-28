from django.contrib import admin
from django.contrib.auth.models import User

from .models import Doctor, Reminder

admin.site.register(Doctor)
admin.site.register(Reminder)
