from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from twilio.twiml.messaging_response import MessagingResponse
from twilio.rest import Client

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
