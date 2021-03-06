# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.utils import timezone
from clock.forms import SignUpForm, ProjectForm
from clock.models import Project


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
		form = ProjectForm()
		start = request.POST.get('start')
		stop = request.POST.get('stop')
		if request.method == 'POST':
			form = ProjectForm(request.POST)
			if form.is_valid():
				name = form.cleaned_data['name']
				project = Project.objects.filter(name=name)
				if start != None:
					if project:
						project.start = timezone.now()
						project.save()
					else:
						data = form.save(commit=False)
						data.start = timezone.now()
						data.save()
					return render(request, 'timer.html',
									{'project': project, 'form': form, 'start': start, 'stop': stop})
				elif stop != None:
					if project:
						project.end = timezone.now()
						project.duration = project.end - project.start
						project.save()
						return render(request, 'timer.html',
									{'project': project, 'form': form, 'start': start, 'stop': stop})
					else:
						data = form.save(commit=False)
						data.end = timezone.now()
						data.duration = data.end - data.start
						data.save()
						new_project = Project.objects.get(name=data.name)
						return render(request, 'timer.html',
									{'project': project, 'form': form, 'start': start, 'stop': stop,
										'new_project': new_project})
			else:
				print '====='
		else:
			return render(request, 'timer.html', {'form': form, 'start': start, 'stop': stop})
	else:
		return redirect('login')


def profile(request, username):
	username = User.objects.get(username=username)
	if request.user.is_authenticated:
		return render(request, 'profile.html', {'username': username})
	else:
		return redirect('login')
