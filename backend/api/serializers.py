from rest_framework import serializers
from ..models import UserInfo, Subscriber, Service, Organization

class UserInfoSerializer(serializers.ModelSerializer):
	class Meta:
		model = UserInfo
		fields = '__all__'
        lookup_field='username'

class SubscriberSerializer(serializers.ModelSerializer):
	class Meta:
		model = Subscriber
		fields = '__all__'
        lookup_field='subscriberid'

class ServiceSerializer(serializers.ModelSerializer):
	class Meta:
		model = Service
		fields = '__all__'
        lookup_field='servicecode'

class OrganizationSerializer(serializers.ModelSerializer):
	class Meta:
		model = Organization
		fields = '__all__'
        lookup_field='orgcode'


        