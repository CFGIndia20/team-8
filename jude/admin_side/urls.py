from django.urls import path, re_path
from admin_side import views

app_name='admin_side'
urlpatterns = [
	path('', views.index, name='index'),
]