from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from twilio.twiml.messaging_response import MessagingResponse
from twilio.rest import Client
import time
from admin_side.models import *
from datetime import datetime
from googletrans import Translator
import random


class Translate:
    def __init__(self):
        self.translator = Translator()
        self.languages = {
                    "hindi":"hi",
                    "bengali":"bn",
                    "english":"en",
                    "gujarati":"gu",
                    "malay":"ms",
                    "malayalam":"ml",
                    "marathi":"mr",
                    "punjabi":"pa",
                    "tamil":"ta",
                    "telegu":"te"
                     }
    def translate(self,string,source,destination):
        return self.translator.translate(string,src = self.languages[source],dest = self.languages[destination]).text



tr = Translate()

def get_data():
        q1 = list(Patients.objects.filter(datetime.now()-checkin_date_time >= datetime(0,0,3)).values("prefered_language"))
        #q1 gives patiends objects with greater than 3 days checking date language
        q2 = list(Patients.objects.filter(datetime.now()-checkin_date_time >= datetime(0,0,3)).values("telephone"))
        #q2 gives phone number
        return q1+q2

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
                                resp.message("Thank you for your feedback")
                        else:
                                op = "Thank you for your response.\n"+questions[numbers[int(num[1])].received]
                                resp.message(op)
    except Exception as ex:
        resp.message(str(ex))
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

#get_data()

account_sid = 'AC32ffcb615c43430096f65348be6fde3e'
auth_token = '156394447a8cbfc44be14c3287a675de'
client = Client(account_sid,auth_token)

questions = ["How was the food?","How was the stay?","How was the cleanliness?"]
mx = len(questions)

numbers = {8638569010:details(),7002566015:details()}
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

Fixes the max wait time

wait_time = 6*60*60
start = time.time()
while(True):
        timeout(numbers,questions)
        time.sleep(wait_time)
        
'''
