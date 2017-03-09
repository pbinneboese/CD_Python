from __future__ import unicode_literals

from django.core.exceptions import ObjectDoesNotExist
import datetime
from datetime import datetime
from datetime import date
from datetime import time
from django.utils import timezone
from django.db import models
from ..LoginReg.models import User

# Create your models Managers here.
class ApptManager(models.Manager):
	def create_appt(self, postData):  # for creating a new appt
		# validate appointment inputs
		errors=[]
		appt_date = postData['appt_date']
		appt_time = postData['appt_time']
		appt_task = postData['appt_task']
		appt_status = postData['appt_status']
		user = postData['user']
		this_date = str(datetime.now().date())
		print "Dates: appt, now", appt_date, this_date
		# validate the date & time represent a current or future date
		if (appt_date < this_date) or (str(appt_date) == ""):
			errors.append('Must enter a current or future date')
		if str(appt_time) == "":
			errors.append('Must enter a time')
		if appt_task == "":
			errors.append('Must enter a task')
		if not errors:	# check for duplicate appointments
			check_appts = self.filter(date=appt_date, time=appt_time)
			if len(check_appts):
				errors.append('This appointment time is already reserved, enter a different time')
		if errors:
			return {'status':False, 'errors':errors}
		else:
			appt = self.create(task=appt_task, date=appt_date, time=appt_time, status=appt_status, user=user)
			return {'status':True, 'appt':appt}

	def update_appt(self, postData):  # for updating an appt
		# validate appointment inputs
		errors=[]
		appt_date = postData['appt_date']
		appt_time = postData['appt_time']
		appt_task = postData['appt_task']
		appt_status = postData['appt_status']
		appt_id = postData['appt_id']
		user = postData['user']
		this_date = str(datetime.now().date())
		print "Dates: appt, now", appt_date, this_date
		# validate the date & time represent a current or future date
		if (appt_date < this_date) or (str(appt_date) == "") :
			errors.append('Must enter a current or future date')
		if str(appt_time) == "":
			errors.append('Must enter a time')
		if appt_task == "":
			errors.append('Must enter a task')
		if not errors:	# check for duplicate appointments
			check_appts = self.filter(date=appt_date, time=appt_time, user=user)
			if len(check_appts):
				errors.append('This appointment time is already reserved, enter a different time')
		if errors:
			return {'status':False, 'errors':errors}
		else:
			appt = self.get(id=appt_id)
			appt.date = appt_date
			appt.time = appt_time
			appt.task = appt_task
			appt.status = appt_status
			appt.save()
			return {'status':True, 'appt':appt}

	def delete_appt(self, postData):  # for deleting an appt
		# validate appointment inputs
		errors=[]
		appt_id = postData['appt_id']
		user = postData['user']
		try:	# check if appt exists
			appt = self.get(id=postData['appt_id'])
		except ObjectDoesNotExist:
			return {'status':False}
		# if appt.user != user:	# ensure this user created the appt
			# return {'status':False}
		appt.delete()	# now delete the appt
		return {'status':True}


# Create your models here.
class Appt(models.Model):
	user = models.ForeignKey(User, related_name="appt_user")
	task = models.CharField(max_length=255)
	date = models.DateField()
	time = models.TimeField()
	status = models.CharField(max_length=255)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)
	objects = ApptManager()
