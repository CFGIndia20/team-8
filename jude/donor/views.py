from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from twilio.twiml.messaging_response import MessagingResponse

@csrf_exempt
def sms_reply(request):
	print("hello")
	"""Respond to incoming calls with a simple text message."""
	# Fetch the message
	msg = request.POST.get('Body')

	#info = .objects.filter(complaint_type='Intercom').order_by('complaint_date')
	# Create reply
	#from django.db.models import OuterRef, Subquery
	#newest = Comment.objects.filter(post=OuterRef('pk')).order_by('-created_at')
	#Post.objects.annotate(newest_commenter_email=Subquery(newest.values('email')[:1]))


	#u = Donor.objects.filter(unitno = msg)

	resp = MessagingResponse()
	resp.message("You said: {}".format(msg))

	return HttpResponse(str(resp))