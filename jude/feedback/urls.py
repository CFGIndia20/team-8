from django.urls import path, re_path
from feedback import views

app_name='feedback'
urlpatterns = [
	path('sms_reply', views.sms_reply, name='sms_reply')
]