# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver


class Profile(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	location = models.CharField(max_length=100, blank=True)
	portfolio = models.CharField(max_length=50, blank=True)
	social_1 = models.CharField(max_length=50, blank=True)
	social_2 = models.CharField(max_length=50, blank=True)
	photo = models.ImageField(blank=True)


@receiver(post_save, sender=User)
def update_user_profile(sender, instance, created, **kwargs):
	if created:
		Profile.objects.create(user=instance)
	instance.profile.save()


class Project(models.Model):
	name = models.CharField(max_length=200, unique=True)
	start = models.DateTimeField()
	end = models.DateTimeField(null=True)
	duration = models.DateTimeField(null=True)