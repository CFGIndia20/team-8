from django.shortcuts import render
from django.http import HttpResponse
from admin_side.models import Patients, PatientFeedback, Questions


def index(request):	
	return render(request,'admin_side/home.html')

# def test(request):
# 	if request.method=='POST':
# 		centre = request.POST['cen']

# 		features= []
# 		ratings = []

# 		q1 = list(Patients.objects.filter(center_name = centre).values('uid'))
# 		uids = [d['uid'] for d in q1]		
# 		rat = list(PatientFeedback.objects.filter(uid__in = uids).values('rating'))
# 		q2 = list(PatientFeedback.objects.filter(uid__in = uids).values('question_id'))
# 		qids = [d['question_id'] for d in q2]
# 		que = list(Questions.objects.filter(question_id__in = qids).values('question'))
# 		features = [d['question'] for d in que]
# 		ratings =[d['rating'] for d in rat]
# 		print(features)
# 		print(ratings)
# 		return render(request,'admin_side/charts.html', {'features':features, 'ratings':ratings})

# 		#return render(request,'admin_side/charts.html', {'features': features, 'ratings':ratings})



def Centre(request):	
	return render(request,'admin_side/Centre.html')


# Create your views here.
