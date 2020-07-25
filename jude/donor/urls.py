#hello
from django.urls import path
from donor import views
app_name='donor'
urlpatterns = [
	path('sms_reply', views.sms_reply, name='sms_reply'),
]