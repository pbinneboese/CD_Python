from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.exceptions import ObjectDoesNotExist
import datetime
from datetime import datetime
from datetime import date
from datetime import time
from django.utils import timezone
from .models import Appt
from ..LoginReg.models import User

# Create your views here.
def dashboard(request):
	print "DASHBOARD"
	# print request.session
	if not 'user_id' in request.session:
		messages.error(request, "Not logged in, please login or register")
		return redirect("LoginReg:index")

	user = User.objects.get(id=request.session['user_id'])
	this_date = datetime.now().date()
	this_time = datetime.now().time()
	today_appts = Appt.objects.filter(user=user, date=this_date).order_by('-time')
	future_appts = Appt.objects.filter(user=user, date__gt=this_date).order_by('time').order_by('date')
	context = {
		'this_date': this_date,
		'this_time': this_time,
		'today_appts': today_appts,
		'future_appts': future_appts
	}
	return render(request, "app1/dashboard.html", context)

def create_appt(request):
	print "CREATE_APPT"
	if request.method != "POST":
		return redirect("app1:dashboard")
	context = {
		'appt_date': request.POST['appt_date'],
		'appt_time': request.POST['appt_time'],
		'appt_task': request.POST['appt_task'],
		'appt_status': "Pending",
		'user': User.objects.get(id=request.session['user_id'])
	}
	response = Appt.objects.create_appt(context)
	if response['status'] == True:
		print "Done"
	else:
		for error in response['errors']:
			messages.error(request, error)
		print "Failed"
	return redirect("app1:dashboard")

def edit_appt(request, appt_id):
	print "EDIT_APPT"
	context = {
		'this_date': datetime.now().date(),
		'this_time': datetime.now().time(),
		'appt': Appt.objects.get(id=appt_id)
	}
	return render(request, "app1/edit.html", context)

def update_appt(request, appt_id):
	print "UPDATE_APPT"
	if request.method != "POST":
		return redirect("app1:dashboard")
	context = {
		'appt_date': request.POST['appt_date'],
		'appt_time': request.POST['appt_time'],
		'appt_task': request.POST['appt_task'],
		'appt_status': request.POST['appt_status'],
		'appt_id': appt_id,
		'user': User.objects.get(id=request.session['user_id'])
	}
	response = Appt.objects.update_appt(context)
	if response['status'] == True:
		print "Done"
	else:
		for error in response['errors']:
			messages.error(request, error)
		print "Failed"
	return redirect("app1:dashboard")

def delete_appt(request, appt_id):
	print "DELETE_APPT"
	context = {
		'appt_id': appt_id,
		'user': User.objects.get(id=request.session['user_id'])
	}
	response = Appt.objects.delete_appt(context)
	if response['status'] == True:
		print "Done"
	else:
		for error in response['errors']:
			messages.error(request, error)
		print "Failed"
	return redirect("app1:dashboard")
