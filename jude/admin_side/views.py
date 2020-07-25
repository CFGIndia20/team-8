from django.shortcuts import render
from django.http import HttpResponse


def index(request):	
	return render(request,'admin_side/test.html')

def test(request):
	return HttpResponse('hello')


def Centre(request):	
	return render(request,'admin_side/Centre.html')


# Create your views here.
