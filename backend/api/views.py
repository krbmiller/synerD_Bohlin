from rest_framework import generics
from ..models import UserInfo, Subscriber, Service, Organization
from .serializers import UserInfoSerializer, SubscriberSerializer, ServiceSerializer, OrganizationSerializer

class UserInfoListView(generics.ListAPIView): 
	queryset = UserInfo.objects.all() 
	serializer_class = UserInfoSerializer

class UserInfoDetailView(generics.RetrieveAPIView): 
	lookup_field = "username"
	queryset = UserInfo.objects.all() 
	serializer_class = UserInfoSerializer

class SubscriberListView(generics.ListAPIView): 
	queryset = Subscriber.objects.all() 
	serializer_class = SubscriberSerializer

class SubscriberDetailView(generics.RetrieveAPIView): 
	lookup_field = "subscriberid"
	queryset = Subscriber.objects.all() 
	serializer_class = SubscriberSerializer

class ServiceListView(generics.ListAPIView): 
	queryset = Service.objects.all() 
	serializer_class = ServiceSerializer

class ServiceDetailView(generics.RetrieveAPIView): 
	lookup_field = "servicecode"
	queryset = Service.objects.all() 
	serializer_class = ServiceSerializer

class OrganizationListView(generics.ListAPIView): 
	queryset = Organization.objects.all() 
	serializer_class = OrganizationSerializer

class OrganizationDetailView(generics.RetrieveAPIView): 
	lookup_field = "orgcode"
	queryset = Organization.objects.all() 
	serializer_class = OrganizationSerializer


