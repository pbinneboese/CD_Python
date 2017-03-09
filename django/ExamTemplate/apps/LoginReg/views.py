from django.shortcuts import render, redirect
from django.contrib import messages
from .models import User
# import arrow

# Create your views here.
def index(request):
	return render(request, "LoginReg/index.html")

def register(request):    # process user registration form
	print "REGISTER"
	if request.method == "POST":
		response = User.objects.register(request.POST)
		if response['status'] == False:
			for error in response['errors']:
				messages.error(request, error)
			return redirect("LoginReg:index")
		else:
			# password is validated, save user_id for session
			this_user = response['user']
			print "THIS USER ", this_user.id
			request.session['user_id'] = this_user.id
			request.session['name'] = this_user.name
			return redirect("app1:dashboard")
	else:
		return redirect("LoginReg:index")

def login(request):    # process user login form
	print "LOGIN"
	if request.method == "POST":
		response = User.objects.login(request.POST)
		if response['status'] == False:
			for error in response['errors']:
				messages.error(request, error)
			return redirect("LoginReg:index")
		else:
			# password is validated, save user_id for session
			this_user = response['user']
			print "THIS USER ", this_user.id
			request.session['user_id'] = this_user.id
			request.session['name'] = this_user.name
			return redirect("app1:dashboard")
	else:
		return redirect("LoginReg:index")

def logout(request):    # process user logout form
	print "LOGOUT"
	if not 'user_id' in request.session:
		messages.error(request, "Not logged in, please login or register")
		return redirect("LoginReg:index")
	if request.method == "POST":
		request.session.clear()
	return redirect("LoginReg:index")
