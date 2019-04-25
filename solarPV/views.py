# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, redirect
from backend.models import UserInfo
import requests

def home(request):
	return render(request, 'solarpv/home.html')

def join(request):
	if request.method == 'POST':
		user = UserInfo()
		user.username = request.POST.get('username')
		user.firstname =  request.POST.get('firstname')
		user.middlename = request.POST.get('middlename')
		user.lastname = request.POST.get('lastname')
		user.dobday = request.POST.get('birthDay')
		user.dobmonth = request.POST.get('birthMonth')
		user.dobyear = request.POST.get('birthYear')
		user.email = request.POST.get('email')
		user.officephone = request.POST.get('phonenum')
		user.cellphone = request.POST.get('cellphonenum')
		user.address1 = request.POST.get('streetaddress')
		user.address2 = request.POST.get('streetaddress2')
		user.city = request.POST.get('city')
		user.state = request.POST.get('state')
		user.zip = request.POST.get('zipcode')
		user.password = request.POST.get('password')
		user.save()
		return render(request, 'solarpv/join.html')
	else:
		return render(request, 'solarpv/join.html')

def signin(request):
	if request.method == 'POST':
		response = requests.get('http://localhost:8000/api/userinfo/'+
			request.POST.get('username')+'/')
		print str(response.status_code)
		userData = response.json()
		#print
		if response.status_code == 404:
			return redirect('/solarpv')
		else:
			return redirect('/admin')
	return render(request, 'solarpv/signin.html')

def dashboard(request):
	return render(request, 'solarpv/dashboard.html')

def members(request):
	response = requests.get('http://localhost:8000/api/subscriber')
	membersData = response.json()
	response = requests.get('http://localhost:8000/api/organization')
	organizationData = response.json()
	return render(request, 'solarpv/members.html', {
		'test': 'this is a test',
		'members': membersData,
		'orgs': organizationData
	})

		
