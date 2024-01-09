from django.shortcuts import render, redirect
from .models import Profile
from .forms import ProfileForm
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout


def user_register(request):
	if request.method=='POST':
		username = request.POST['username']
		email = request.POST.get('email')
		first_name = request.POST['first_name']
		last_name = request.POST['last_name']
		password1 = request.POST['password1']
		password2 = request.POST['password2']

		if password1 == password2:
			user = User.objects.create_user(username, email, password1)
			user.first_name=first_name
			user.last_name=last_name
			user.save()
			return redirect("accounts:login")
		else:
			messages.error(request, "Passwords do not match.")
			return redirect("accounts:register")
	else:
		return render(request, "accounts/register.html")
	

def user_login(request):
	if request.method=='POST':
		username = request.POST['username']
		password = request.POST['password']

		user=authenticate(username=username, password=password)

		if user is not None:
			login(request, user)
			messages.success(request, "Successfully logged in.")
			return redirect('index')
		else:
			messages.error(request, "Invalid Credential")
		return render(request, "polls/index.html")
	return render(request, "accounts/login.html")

def user_logout(request):
	logout(request)
	messages.success(request, "Successfully logged out.")
	return redirect("accounts:login")