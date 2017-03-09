from __future__ import unicode_literals

from django.db import models
import datetime
from datetime import datetime
from datetime import date
from datetime import time
from django.utils import timezone
import bcrypt
import re

# EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
NAME_REGEX = re.compile(r'^[a-zA-Z ][a-zA-Z ]+$')
USERNAME_REGEX = re.compile(r'^[a-zA-Z][a-zA-Z]+$')

# Create your models Managers here.
class UserManager(models.Manager):
	def register(self, postData):  # for registering a new user
		errors = []
		# Validate all form data
		# name, username lengths
		if len(postData['name']) < 3:
			errors.append('Name: must be at least 3 characters')
		if len(postData['username']) < 3:
			errors.append('Username: must be at least 3 characters')
		# name, username letters only
		if not NAME_REGEX.match(postData['name']):
			errors.append('Name: use letters and spaces only')
		if not NAME_REGEX.match(postData['username']):
			errors.append('Username: use letters only, no spaces')
		check_user = self.filter(username=postData['username'])
		if len(check_user) > 0:
			errors.append('Username already registered, please login')
		# Password - at least 8 characters, and that it was submitted
		if len(postData['password']) < 8:
			errors.append('Password: must be at least 8 characters')
		# Passwords match
		if not postData['password'] == postData['password_confirmation']:
			errors.append('Passwords do not match, please re-enter')
		# Date of Birth - Valid Date format, and that it was submitted
		this_date = str(datetime.now().date())
		if (postData['birthdate'] >= this_date) or (len(postData['birthdate']) == 0):
			errors.append('Birthdate must be earlier than today, please re-enter')

		if errors:  # If we fail the validations
			return {'status':False, 'errors':errors}
		else:  # Successfully Registered
			# encrypt password
			password = str(postData['password'])
			hashed_pw = bcrypt.hashpw(password, bcrypt.gensalt())
			# create our user
			this_user = self.create(name=postData['name'], username=postData['username'], birthdate=postData['birthdate'], password=hashed_pw)
			print "NEW USER= ", this_user.id
			return {'status':True, 'user':this_user}

	def login(self, postData):  # for validating a user login
		errors = []
		# check for user in database
		try:
			this_user = self.get(username=postData['username'])
		except:
			errors.append('Username not registered, try again')
		else:
			# compare password with stored encrypted password
			password = str(postData['password'])
			hashed_pw = str(this_user.password)
			if bcrypt.hashpw(password, hashed_pw) != hashed_pw:
				errors.append('Password invalid, try again')

		if errors:  # If we fail the validations
			return {'status':False, 'errors':errors}
		else:  # Successfully Logged In
			print "LOGGED IN= ", this_user.id
			return {'status':True, 'user':this_user}

# Create your models here.
class User(models.Model):
	name = models.CharField(max_length=255)
	username = models.CharField(max_length=255)
	birthdate = models.DateField()
	password = models.CharField(max_length=255)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)
	objects = UserManager()
