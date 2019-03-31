# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render

def home(request):
	return render(request, 'solarpv/home.html')

def join(request):
	return render(request, 'solarpv/join.html')

def signin(request):
	return render(request, 'solarpv/signin.html')

def dashboard(request):
	return render(request, 'solarpv/dashboard.html')
