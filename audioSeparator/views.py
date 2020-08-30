from django_twilio.decorators import twilio_view
from twilio.twiml.messaging_response import MessagingResponse,Message
# Create your views here.


@twilio_view
def smsView(request):
    r = MessagingResponse()
    r.message("Todo en orden")
    return r