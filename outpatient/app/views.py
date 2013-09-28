from django.views.generic import TemplateView, CreateView, UpdateView
from .models import Doctor
from django.http import HttpResponseRedirect
from .forms import RegistrationForm
from django.contrib.auth.models import User

from django.shortcuts import render_to_response
from django.template import RequestContext

from django.contrib import messages
from .models import Reminder, Doctor
from django_twilio.decorators import twilio_view
import twilio.twiml

@twilio_view
def sms(request):
    sender = request.POST.get('From')
    body = request.POST.get('Body', '')

    doctors = Doctor.objects.all()

    r = twilio.twiml.Response()
    r.sms("+55432344322: Botswana Wildlife Training Institute")
    return r

class Register(CreateView):
	form_class = RegistrationForm
	template_name = 'register.html'
	model = Doctor
	success_url = '/welcome/'

	def form_valid(self, form):
		print(form.__dict__)
		self.request.session['doctor'] = form.cleaned_data['name']
		return super(Register, self).form_valid(form)

def welcome(request):
	doctor = request.session.get('doctor')
	doctor = Doctor.objects.get(name=doctor)
	context = {"doctor": doctor, "reminders": Reminder.objects.filter(doctor=doctor)}
	return render_to_response('welcome.html', RequestContext(request, context))
