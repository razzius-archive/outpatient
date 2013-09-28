from app.models import Reminder
from django.core.management.base import NoArgsCommand, CommandError
from datetime import datetime, timedelta
from twilio.rest import TwilioRestClient

class Command(NoArgsCommand):
    help = 'Sends all pending reminders that need to be sent'

    def handle_noargs(self, **options):
        to_send = Reminder.objects.filter(scheduled_time__gte=datetime.now()-timedelta(hours=25))
        to_send = to_send.filter(sent24=False)

        for reminder in to_send:
            if reminder.sent24==False:
                client = TwilioRestClient()

                message = client.sms.messages.create(
                        body = "Dr Reminder 4 tomorrow: %s" % reminder.msg,
                        to=reminder.recipient, from_="+12156004771")
                reminder.sent24 = True
                reminder.save()
                print message.sid

        
        print len(to_send)
