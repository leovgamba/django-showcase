from django.shortcuts import render

from django.contrib import auth

from django.core.context_processors import csrf

def login(request):
	context = {}
	context.update(csrf(request))
	return render(request, 'sauth/login.html', context)

def authenticate(request):
	username = request.POST.get('username', '')
	password = request.POST.get('password', '')

	user = auth.authenticate(username=username, password=password)

	if user is None:
		print("wrong pass or user!")
		return render(request, 'sauth/invalid.html')
	else:
		auth.login(request, user)
		print("nice")
		return render(request, 'sauth/loggedin.html')
