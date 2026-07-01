from django.shortcuts import render, redirect
from django.contrib.auth import login as auth_login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import RegisterForm, LoginForm, UserUpdateForm, ProfileUpdateForm

def register(request):

	if request.method == 'POST':
		form = RegisterForm(request.POST)

		if form.is_valid():
			form.save()

			fname = form.cleaned_data.get('first_name')
			lname = form.cleaned_data.get('last_name')

			messages.success(
					request,
					f'Congratulations {fname} {lname}! Your account has been created successfully.'
			)

			return redirect('users:login')

		messages.error(
			request,
			"Please correct the errors below."
		)

	else:
		form = RegisterForm()

	return render(
		request,
		"users/register_form.html",
		{"form": form}
	)


def login(request):
	if request.method == 'POST':
		form = LoginForm(request, data=request.POST)
		if form.is_valid():
			user = form.get_user()
			auth_login(request, user)

			messages.success(
					request,
					f'Hello {user.username}!'
			)

			return redirect('home')
		else:
			messages.error(request, 'Please correct the errors below.')
	else:
		form = LoginForm()
	return render(request, 'users/login_form.html', {'form': form})

@login_required
def user_logout(request):
	logout(request)
	return redirect('home')


@login_required
def my_profile(request):
	user = request.user
	return render(request, 'users/my_profile.html', {'user': user})

@login_required
def edit_profile(request):
	if request.method == 'POST':
		user_form = UserUpdateForm(request.POST, instance=request.user)
		profile_form = ProfileUpdateForm(request.POST, request.FILES, instance=request.user.userprofile)

		if user_form.is_valid() and profile_form.is_valid():
			user_form.save()
			profile_form.save()
			messages.success(request, 'Your profile has been updated successfully.')
			return redirect('users:my_profile')
		else:
			messages.error(request, 'Please correct the errors below.')

	else:
		user_form = UserUpdateForm(instance=request.user)
		profile_form = ProfileUpdateForm(instance=request.user.userprofile)

	return render(request, 'users/edit_profile.html', {'user_form': user_form, 'profile_form': profile_form})
