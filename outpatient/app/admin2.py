from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth.models import User

from .models import Doctor, Reminder

import djadmin2


class UserAdmin2(djadmin2.ModelAdmin2):
    create_form_class = UserCreationForm
    update_form_class = UserChangeForm


#  Register each model with the admin
# djadmin2.default.register(Doctor)
# djadmin2.default.register(Reminder)
# djadmin2.default.register(User, UserAdmin2)