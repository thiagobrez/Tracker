# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, redirect
from clock.models import User


def index(request):
	if request.user.is_authenticated:
		return redirect('/home')
	else:
		pass
	return render(request, 'index.html', {})


def home(request):
	return render(request, 'home.html', {})


def timer(request):
	if request.method == 'POST':
		pass



def profile(request, username):
	username = User.objects.get(username=username)
	if username.is_authenticated:
		return render(request, 'profiles.html')
	else:
		pass