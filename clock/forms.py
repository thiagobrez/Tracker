from django import forms
from models import User, Profile


class UserForm(forms.ModelForm):
	class Meta:
		model = User
		fields = ('first_name', 'last_name', 'email')


class ProfileForm(forms.ModelForm):
	class Meta:
		model = Profile
		fields = ('location', 'portfolio', 'social_1', 'social_2', 'photo')