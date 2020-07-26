from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from twilio.twiml.messaging_response import MessagingResponse
from twilio.rest import Client
<<<<<<< HEAD
import time

class details:
        def __init__(self):
                self.received = 0
                self.time = None
                self.retries = 0
=======

class Send:
    def __init__(self):
        self.account_sid = 'AC32ffcb615c43430096f65348be6fde3e'
        self.auth_token = '156394447a8cbfc44be14c3287a675de'
        self.client = Client(self.account_sid,self.auth_token)
    def send(self,number,message,details):
        #todo encryption
        message = self.client.messages.create(
                                      from_='whatsapp:+14155238886',
                                      body=message,
                                      to='whatsapp:'+"+91"+str(number)
                                  )
>>>>>>> f0922e63e3568265e71f550b2b7499076c251b31

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

<<<<<<< HEAD
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
=======
#timeout
#TODO : GET QUESTIONS,NUMBERS FROM DB WITH LANGUAGE
#Assuming 2 feedback questions

questions = ["test1","test2"]
mx = len(questions)
numbers = {9831788273:[0,None,0],8638569010:[0,None,0]}
#map : key -> number : value [replies,Date-Time,Iterations]

sd = Send()

for i in numbers:
    if(numbers[i][0] == mx): 
        continue
    sd.send(i,questions[numbers[i][0]],numbers)


@csrf_exempt
def sms_reply(request):
	# Fetch the message
	num = request.POST.get('Body')
	#num = str(request.form.get("From")).split("+91")
    resp = MessagingResponse()
    try:
        stars = int(request.POST.get('Body'))
        stars = min(stars,5)
        stars = max(stars,0)
        category[sd.numbers[int(num[1])][0]] += stars
        sd.numbers[int(num[1])][0] += 1
        if(sd.numbers[int(num[1])][0] == 2):
            resp.message("Thank you for your Feedback")
        else:
            op = "Thank you for your response.\n"+sd.questions[sd.numbers[int(num[1])][0]]
            resp.message(op)
    except Exception as ex:
        resp.message(str(ex))
    finally:
        return HttpResponse(str(resp))
>>>>>>> f0922e63e3568265e71f550b2b7499076c251b31
