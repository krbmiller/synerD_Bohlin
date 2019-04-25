from django.conf.urls import url, include
from django.contrib import admin
from django.views.generic.base import RedirectView

from . import views

urlpatterns = [
	url(r'^$', views.home, name='home'),
	url(r'^admin/', admin.site.urls, name='admin'),
	url(r'^join/', views.join, name='join'),
	url(r'^signin/', views.signin, name='signin'),
	url(r'^dashboard/',views.dashboard, name='dashboard'),
	url(r'^members/',views.members, name='members')
]