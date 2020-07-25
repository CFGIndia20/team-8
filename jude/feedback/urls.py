from django.urls import path, re_path
from feedback import views

app_name='feedback'
urlpatterns = [
	path('feedback_processing', views.feedback_processing, name='feedback_processing'),
]