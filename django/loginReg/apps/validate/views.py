from django.shortcuts import render, redirect
from django.contrib import messages
from .models import User

# Create your views here.
def index(request):
	return render(request, "validate/index.html")

def register(request):    # process user registration form
	if request.method == "POST":
		response = User.objects.register(request.POST)
		if response['status'] == False:
			for error in response['errors']:
				messages.error(request, error)
			return redirect("/")
		else:
			# password is validated, save user_id for session
			this_user = response['user']
			print "THIS USER ", this_user.id
			request.session['user_id'] = this_user.id
			request.session['first_name'] = this_user.first_name
			return redirect("/success")
	else:
		return redirect("/")

def login(request):    # process user login form
	if request.method == "POST":
		response = User.objects.login(request.POST)
		if response['status'] == False:
			for error in response['errors']:
				messages.error(request, error)
			return redirect("/")
		else:
			# password is validated, save user_id for session
			this_user = response['user']
			print "THIS USER ", this_user.id
			request.session['user_id'] = this_user.id
			request.session['first_name'] = this_user.first_name
			return redirect("/success")
	else:
		return redirect("/")

def success(request):
	return render(request, "validate/success.html")
