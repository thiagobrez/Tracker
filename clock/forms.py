from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from models import Profile, Project


class UserForm(forms.ModelForm):
	class Meta:
		model = User
		fields = ('first_name', 'last_name', 'email')


class ProfileForm(forms.ModelForm):
	class Meta:
		model = Profile
		fields = ('location', 'portfolio', 'social_1', 'social_2', 'photo')


class SignUpForm(UserCreationForm):
	class Meta:
		model = User
		fields = ('username', 'email', 'password1', 'password2', 'first_name', 'last_name')


class ProjectForm(forms.ModelForm):
	class Meta:
		model = Project
		fields = ('name',)
