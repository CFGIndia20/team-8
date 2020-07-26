from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from twilio.twiml.messaging_response import MessagingResponse
from admin_side.models import Patients, Donor
from datetime import date
from dateutil.relativedelta import relativedelta
today = date.today()



six_months = date.today() + relativedelta(months=-6)

@csrf_exempt
def sms_reply(request):
	msg = request.POST.get('Body')

	q1 = list(Donor.objects.filter(phoneno = int(msg)).values('unitno'))
	unitnos = [int(d['unitno']) for d in q1]	
	q2 = list(Patients.objects.filter(unitno__in = unitnos).values('uid'))
	uids = [str(d['uid']) for d in q2]	
	q3 = list(Patients.objects.filter(unitno__in = unitnos).values('name'))
	names = [d['name'] for d in q3]	
	l=[]
	msg = "Hi...These are the uids and names of children that have stayed in the unit you funded in the last six months: "

	for i,j in zip(uids,names):
		msg = msg + i + " : "+j + " " 
	resp = MessagingResponse()
	resp.message(msg)

	return HttpResponse(str(resp))

