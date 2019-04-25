# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import Subscriber, Organization, Service, UserInfo, SubscriptionType, Officer, Office, OrganizationMember

@admin.register(Subscriber)
class SubscriberAdmin(admin.ModelAdmin):
	list_display = ['subscriberid','servicecode_id']

@admin.register(Organization)
class SubscriberAdmin(admin.ModelAdmin):
	list_display = ['orgcode','orgname']

@admin.register(Service)
class SubscriberAdmin(admin.ModelAdmin):
	list_display = ['servicecode','servicename']

@admin.register(UserInfo)
class SubscriberAdmin(admin.ModelAdmin):
	list_display = ['username','firstname','lastname']

@admin.register(SubscriptionType)
class SubscriberAdmin(admin.ModelAdmin):
	list_display = ['subscriptiontypecode']

@admin.register(Officer)
class SubscriberAdmin(admin.ModelAdmin):
	list_display = ['subscriberid','officecode']

@admin.register(Office)
class SubscriberAdmin(admin.ModelAdmin):
	list_display = ['officecode','officename']

@admin.register(OrganizationMember)
class SubscriberAdmin(admin.ModelAdmin):
	list_display = ['orgcode','subscriberid','startdate','enddate']