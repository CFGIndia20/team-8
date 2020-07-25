#hello
app_name='donor'
urlpatterns = [
	path('sms_reply', views.sms_reply, name='sms_reply'),
]