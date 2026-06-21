from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django import forms
from .models import UserProfile

class RegisterForm(UserCreationForm):
	class Meta:
		model = User
		fields = [
			'username',
			'email',
			'first_name',
			'last_name',
			'password1',
			'password2',
		]
		def __init__(self, *args, **kwargs):
			super().__init__(*args, **kwargs)

			for field in self.fields.values():
				field.widget.attrs.update({
					'class': 'w-full border border-gray-300 rounded-xl p-3 focus:ring-2 focus:ring-lime-500 focus:outline-none'
				})


class LoginForm(AuthenticationForm):

	def __init__(self, *args, **kwargs):
		super().__init__(*args, **kwargs)

		for field in self.fields.values():
			field.widget.attrs.update({
				'class': 'w-full border border-gray-300 rounded-xl p-3 focus:ring-2 focus:ring-lime-500 focus:outline-none'
			})


class UserUpdateForm(forms.ModelForm):
	class Meta:
		model = User
		fields = [
			'first_name',
			'last_name',
			'email',
		]

		widgets = {
			'first_name': forms.TextInput(attrs={
				'class': 'w-full border border-gray-300 rounded-xl p-3 focus:ring-2 focus:ring-lime-500'
			}),
			'last_name': forms.TextInput(attrs={
				'class': 'w-full border border-gray-300 rounded-xl p-3 focus:ring-2 focus:ring-lime-500'
			}),
			'email': forms.EmailInput(attrs={
				'class': 'w-full border border-gray-300 rounded-xl p-3 focus:ring-2 focus:ring-lime-500'
			}),
		}

class ProfileUpdateForm(forms.ModelForm):
	class Meta:
		model = UserProfile
		fields = ['bio', 'website', 'avatar']

		widgets = {
			'bio': forms.Textarea(attrs={
					'rows': 4,
					'class': 'w-full border border-gray-300 rounded-xl p-3 focus:ring-2 focus:ring-lime-500'
			}),
			'website': forms.URLInput(attrs={
					'class': 'w-full border border-gray-300 rounded-xl p-3 focus:ring-2 focus:ring-lime-500'
			}),
		}