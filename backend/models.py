# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


class Office(models.Model):
    officecode = models.CharField(primary_key=True, max_length=50) 
    officename = models.CharField(unique=True, max_length=250)   
    attribution = models.CharField(max_length=500, null=True)


class Organization(models.Model):
    orgcode = models.CharField(primary_key=True, max_length=100)  
    orgname = models.CharField(max_length=250)  
    description = models.CharField(max_length=500)
    datejoined = models.DateTimeField(null=True)  
    address1 = models.CharField(max_length=250, null=True)
    address2 = models.CharField(max_length=250, null=True)
    city = models.CharField(max_length=100, null=True)
    state = models.CharField(max_length=100, null=True)
    zip = models.CharField(max_length=100, null=True)
    phonenumber = models.CharField(max_length=100, null=True)  


class UserInfo(models.Model):
    username = models.CharField(primary_key=True, max_length=100)  
    firstname = models.CharField(max_length=100)  
    middlename = models.CharField(max_length=100, null=True)  
    lastname = models.CharField(max_length=100)  
    dobday = models.IntegerField(null=True)  
    dobmonth = models.IntegerField(null=True)  
    dobyear = models.IntegerField(null=True)  
    email = models.CharField(max_length=250)
    officephone = models.CharField(max_length=100, null=True)  
    cellphone = models.CharField(max_length=100, null=True)  
    address1 = models.CharField(max_length=250, null=True)
    address2 = models.CharField(max_length=250, null=True)
    city = models.CharField(max_length=250, null=True)
    state = models.CharField(max_length=100, null=True)
    zip = models.CharField(max_length=100, null=True)
    employername = models.CharField(max_length=250, null=True)  
    empaddress1 = models.CharField(max_length=250, null=True)  
    empaddress2 = models.CharField(max_length=250, null=True)  
    empcity = models.CharField(max_length=250, null=True)  
    empstate = models.CharField(max_length=100, null=True)  
    empzip = models.CharField(max_length=100, null=True)  
    empphone = models.CharField(max_length=100, null=True)  
    jobtitle = models.CharField(max_length=250, null=True)  
    governmentidtype = models.CharField(max_length=100, null=True)  
    governmentidnum = models.CharField(max_length=100, null=True)  
    govidissuecountry = models.CharField(max_length=100, null=True)  
    govidissuestate = models.CharField(max_length=100, null=True)  
    govidissuedate = models.DateTimeField(null=True)  
    govidissueexpire = models.DateTimeField(null=True)   
    password = models.CharField(max_length=100, null=True)


class Service(models.Model):
    servicecode = models.CharField(primary_key=True, max_length=100)  
    servicename = models.CharField(max_length=250)  
    servicedescription = models.CharField(max_length=250, null=True)  
    premium = models.DecimalField(max_digits=19,decimal_places=10)
    allocation = models.IntegerField(null=True)

class SubscriptionType(models.Model):
	subscriptiontypecode = models.CharField(primary_key=True, max_length=50)
	subscriptiontypename = models.CharField(max_length=250, null=True)


class Subscriber(models.Model):
    subscriberid = models.IntegerField(primary_key=True)  
    servicecode = models.ForeignKey(Service, on_delete=models.CASCADE)  
    requestdate = models.DateTimeField()  
    startdate = models.DateTimeField(null=True)  
    enddate = models.DateTimeField(null=True)  
    motifcancellation = models.CharField(max_length=250, null=True)  
    subscriptiontype = models.ForeignKey(SubscriptionType, on_delete=models.CASCADE)
    username = models.ForeignKey(UserInfo, on_delete=models.CASCADE)
    beneficiaryid = models.ForeignKey('self', on_delete=models.CASCADE, null=True)


class Officer(models.Model): 
    subscriberid = models.ForeignKey(Subscriber, on_delete=models.CASCADE)  
    officecode = models.ForeignKey(Office, on_delete=models.CASCADE) 
    startdate = models.DateTimeField(null=True)  
    enddate = models.DateTimeField(null=True)  



class OrganizationMember(models.Model):
	is_delegate = (
		(0, 'No'),
		(1, 'Yes')
	)
	orgcode = models.ForeignKey(Organization, on_delete=models.CASCADE)
	subscriberid = models.ForeignKey(Subscriber, on_delete=models.CASCADE)
	startdate = models.DateTimeField(null=True)
	enddate = models.DateTimeField(null=True)
	nativecountry = models.CharField(max_length=100, null=True)
	citizenship = models.CharField(max_length=250, null=True)
	isdelegate = models.IntegerField(choices=is_delegate)


class TransferSubscription(models.Model):
	transferid = models.IntegerField(primary_key=True)
	subscriberid = models.ForeignKey(Subscriber, on_delete=models.CASCADE)
	transferfrom = models.ForeignKey(Organization, related_name='transferfrom', on_delete=models.CASCADE)
	transferto = models.ForeignKey(Organization, related_name='transferto', on_delete=models.CASCADE)
	requestdate = models.DateTimeField()
	transferdate = models.DateTimeField(null=True)









