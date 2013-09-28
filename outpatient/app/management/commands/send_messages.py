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
            if reminder.sent24=False:
                account_sid = ''
                auth_token = ''

                client = TwilioRestClient(account_sid, auth_token)

                message = client.sms.messages.create(
                        body = "Dr Reminder 4 tomorrow: %s" % reminder.msg,
                        to=recipient,
                        from="+12156004771")
                print message.sid

        
        print len(to_send)
