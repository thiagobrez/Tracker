# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect
from clock.models import User
from clock.forms import SignUpForm


def index(request):
	if request.user.is_authenticated:
		return redirect('/home')
	else:
		return render(request, 'index.html', {})


def home(request):
	if request.user.is_authenticated:
		return render(request, 'home.html', {})
	else:
		return redirect('login')


def signup(request):
	if request.method == 'POST':
		form = SignUpForm(request.POST)
		if form.is_valid():
			# TRATAR AQUI DE INSERIR O USUARIO NOVO EM UM GRUPO
			form.save()
			username = form.cleaned_data.get('username')
			raw_password = form.cleaned_data.get('password1')
			user = authenticate(username=username, password=raw_password)
			login(request, user)
			return redirect('home')
	else:
		form = SignUpForm()
		return render(request, 'signup.html', {'form': form})


def timer(request):
	if request.user.is_authenticated:
		if request.method == 'POST':
			pass
		else:
			return render(request, 'timer.html', {})
	else:
		return redirect('login')


# RESOLVER
def profile(request, username):
	username = User.objects.get(username=username)
	if username.is_authenticated:
		return render(request, 'profile.html')
	else:
		pass