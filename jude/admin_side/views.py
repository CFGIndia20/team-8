from django.shortcuts import render
from django.http import HttpResponse


def index(request):	
	return render(request,'admin_side/home.html')



def Centre(request):	
	return render(request,'admin_side/Centre.html')


# Create your views here.
