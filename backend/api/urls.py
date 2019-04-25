from django.conf.urls import url, include
from . import views

app_name = 'backend'
urlpatterns = [ 
	url(r'^userinfo/(?P<username>[\w\-]+)/$', views.UserInfoDetailView.as_view(), name='userinfo_detail'),
	url(r'^userinfo/', views.UserInfoListView.as_view(), name='userinfo_list'), 
	
	url(r'^subscriber/(?P<subscriberid>[\w\-]+)/$', views.SubscriberDetailView.as_view(), name='subscriber_detail'),
	url(r'^subscriber/', views.SubscriberListView.as_view(), name='subscriber_list'), 
	
	url(r'^service/(?P<servicecode>[\w\-]+)/$', views.ServiceDetailView.as_view(), name='service_detail'),
	url(r'^service/', views.ServiceListView.as_view(), name='service_list'), 
	
	url(r'^organization/(?P<orgcode>[\w\-]+)/$', views.OrganizationDetailView.as_view(), name='organization_detail'),
	url(r'^organization/', views.OrganizationListView.as_view(), name='organization_list') 
	
]
