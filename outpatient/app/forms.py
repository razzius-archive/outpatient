from django import forms
from django.contrib.auth.models import User

from crispy_forms.layout import Layout, Submit, Div, Field
from crispy_forms.helper import FormHelper

from .models import Doctor

class RegistrationForm(forms.ModelForm):
	def __init__(self, *args, **kwargs):
		super(RegistrationForm, self).__init__(*args, **kwargs)
		self.helper = FormHelper(self)
		self.helper.add_input(Submit('submit', "Submit"))
		self.helper.form_method = 'post'

	class Meta:
		model = Doctor
		fields = ['name', 'location']

class UserForm(forms.ModelForm):
    class Meta:
        model = User 