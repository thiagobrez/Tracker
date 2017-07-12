# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
from clock.models import User


def index(request):
	return render(request, 'index.html', {})


def profile(request, username):
	u = User.objects.get(username=username)
	return render(request, 'profile.html', {'u': u})