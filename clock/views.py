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
	if request.user.is_authenticated:
		if request.method == 'POST':
			pass
		else:
			return render(request, 'timer.html', {})
	# else:
		# return render() redirecionar para tela de sign up?


def profile(request, username):
	username = User.objects.get(username=username)
	if username.is_authenticated:
		return render(request, 'profile.html')
	else:
		pass