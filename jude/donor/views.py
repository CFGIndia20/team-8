from django.shortcuts import render
from django.http import HttpResponse

def sms_reply():
    """Respond to incoming calls with a simple text message."""
    # Fetch the message
    msg = request.form.get('Body')
    
    # Create reply
    resp = MessagingResponse()
    resp.message("You said: {}".format(msg))

    return str(resp)

# Create your views here.
