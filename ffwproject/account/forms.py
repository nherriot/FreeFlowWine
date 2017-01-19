from django import forms


from .models import UserProfile
from django.contrib.auth.models import User

class UserForm(forms.ModelForm):
	password = forms.CharField(widget=forms.PasswordInput())
	class Meta:
		model = User
		fields = ('username', 'email', 'password')


class UserProfileForm(forms.ModelForm):
	class Meta:
		model = UserProfile

		fields = [
				'first_name',
				'last_name',
				'address',
				'address_1',
				'city',
				'post_code',
				'image',
				'bio',
			]
			

