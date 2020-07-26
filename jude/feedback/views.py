from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from twilio.twiml.messaging_response import MessagingResponse
from twilio.rest import Client
import time

class details:
        def __init__(self):
                self.received = 0
                self.time = None
                self.retries = 0

def send(number,message,det):
	#todo encryption
        client.messages.create(
		from_='whatsapp:+14155238886',
		body=message,
		to='whatsapp:'+"+91"+str(number)
		)
        det.time = time.time()
        
	
@csrf_exempt
def sms_reply(request):
	num = str(request.POST.get("From")).split("+91")
	resp = MessagingResponse()
	try:
                stars = ord(request.POST.get('Body'))
                if(stars not in ratings_emoji):
                        #raise Exception("Incorrect Option")
                        resp.message("Incorrect Option")
                        return HttpResponse(str(resp))
                stars = ratings_emoji[stars]
                numbers[int(num[1])].retries = 0
                if(numbers[int(num[1])].received == 2):
                        resp.message("We have already received your feedback")
                else:
                        category[numbers[int(num[1])].received] += stars
                        ct[numbers[int(num[1])].received] += 1
                        numbers[int(num[1])].received += 1
                        if(numbers[int(num[1])].received == 2):
                                resp.message("Thank you for your Feedback")
                        else:
                                op = "Thank you for your response.\n"+questions[numbers[int(num[1])].received]
                                resp.message(op)
	except:
		resp.message("Please Try Again")
	finally:
		return HttpResponse(str(resp))

def timeout(numbers,questions):
        for i in numbers:
                if(numbers[i].retries == max_retries):
                        del numbers[i]
                        continue
                if(time.time() >= numbers[i].time + (wait_time)):
                        numbers[i].retries += 1
                        numbers[i].time = time.time()
                        send(i,questions[numbers[i].received],numbers)

account_sid = 'AC32ffcb615c43430096f65348be6fde3e'
auth_token = '156394447a8cbfc44be14c3287a675de'
client = Client(account_sid,auth_token)

questions = ["test1","test2"]
mx = len(questions)



numbers = {8727096226:details(),8638569010:details(),7002566015:details()}
category = [0,0]
ct = [0,0]

max_retries = 2


#emoji ranking : ord(emoji): score
ratings_emoji = {128513:5,
                 128516:4,
                 128578:3,
                 128533:2,
                 128577:1
                 }

for i in numbers:
    if(numbers[i].received == mx):
        del numbers[i]
        continue
    send(i,questions[numbers[i].received],numbers[i])

'''
wait_time = 6*60*60
start = time.time()
while(True):
        timeout(numbers,questions)
        time.sleep(wait_time)
        
'''
