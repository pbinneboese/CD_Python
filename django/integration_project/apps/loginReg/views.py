from django.shortcuts import render, redirect
from django.contrib import messages
from .models import User

# Create your views here.
def index(request):
	return render(request, "loginReg/index.html")

def register(request):    # process user registration form
	if request.method == "POST":
		response = User.objects.register(request.POST)
		if response['status'] == False:
			for error in response['errors']:
				messages.error(request, error)
			return redirect("loginReg:index")
		else:
			# password is validated, save user_id for session
			this_user = response['user']
			print "THIS USER ", this_user.id
			request.session['user_id'] = this_user.id
			request.session['first_name'] = this_user.first_name
			return redirect("loginReg:success")
	else:
		return redirect("loginReg:index")

def login(request):    # process user login form
	if request.method == "POST":
		response = User.objects.login(request.POST)
		if response['status'] == False:
			for error in response['errors']:
				messages.error(request, error)
			return redirect("loginReg:index")
		else:
			# password is validated, save user_id for session
			this_user = response['user']
			print "THIS USER ", this_user.id
			request.session['user_id'] = this_user.id
			request.session['first_name'] = this_user.first_name
			return redirect("loginReg:success")
	else:
		return redirect("loginReg:index")

def success(request):
	print request.session
	if not 'user_id' in request.session:
		messages.error(request, "Not logged in, please login or register")
		return redirect("loginReg:index")
	else:
		return render(request, "loginReg/success.html")

def logout(request):    # process user logout form
	if request.method == "POST":
		request.session.clear()
	return redirect("loginReg:index")
