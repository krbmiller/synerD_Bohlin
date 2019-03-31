from django.conf.urls import url, include

from . import views

urlpatterns = [
	url(r'^$', views.home, name='home'),
	url(r'^join/', views.join, name='join'),
	url(r'^signin/', views.signin, name='signin'),
	url(r'^dashboard/',views.dashboard, name='dashboard')
]