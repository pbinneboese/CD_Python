# from __future__ import unicode_literals

from django.db import models
import bcrypt
import re

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
NAME_REGEX = re.compile(r'^[a-zA-Z][a-zA-Z]+$')

# Create your models here.
class UserManager(models.Manager):
	def register(self, postData):  # for registering a new user
		errors = []
		# Validate all form data
		# first_name, last_name lengths
		if len(postData['first_name']) < 2:
			errors.append('First name: must be at least 2 characters')
		if len(postData['last_name']) < 2:
			errors.append('Last name: must be at least 2 characters')
		# first_name, last_name letters only
		if not NAME_REGEX.match(postData['first_name']):
			errors.append('First name: use letters only')
		if not NAME_REGEX.match(postData['last_name']):
			errors.append('Last name: use letters only')
		# Email - Valid Email format, and that it was submitted
		if not EMAIL_REGEX.match(postData['email']):
			errors.append('Not a valid email address, please re-enter')
		check_user = self.filter(email=postData['email'])
		if check_user:
			errors.append('Email already registered, please login')
		# Password - at least 8 characters, and that it was submitted
		if len(postData['password']) < 8:
			errors.append('Password: must be at least 8 characters')
		# Passwords match
		if not postData['password'] == postData['password_confirmation']:
			errors.append('Passwords do not match, please re-enter')

		if errors:  # If we fail the validations
			# for error in errors:
				# print "ERROR ", type(error), error
			return {'status':False, 'errors':errors}
		else:  # Successfully Registered
			# encrypt password
			password = str(postData['password'])
			hashed_pw = bcrypt.hashpw(password, bcrypt.gensalt())
			# print "PASSWORD= ", hashed_pw
			# create our user
			this_user = self.create(first_name=postData['first_name'], last_name=postData['last_name'], email=postData['email'], password=hashed_pw)
			print "NEW USER= ", this_user.id
			return {'status':True, 'user':this_user}

	def login(self, postData):  # for validating a user login
		errors = []
		# check for user in database
		try:
			this_user = self.get(email=postData['email'])
		except:
			errors.append('Email not registered, try again')
		else:
			# compare password with stored encrypted password
			password = str(postData['password'])
			hashed_pw = str(this_user.password)
			if bcrypt.hashpw(password, hashed_pw) != hashed_pw:
				errors.append('Password invalid, try again')

		if errors:  # If we fail the validations
			# for error in errors:
				# print "ERROR ", type(error), error
			return {'status':False, 'errors':errors}
		else:  # Successfully Logged In
			print "LOGGED IN= ", this_user.id
			return {'status':True, 'user':this_user}

class User(models.Model):
	first_name = models.CharField(max_length=50)
	last_name = models.CharField(max_length=50)
	email = models.CharField(max_length=100)
	password = models.CharField(max_length=255)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)
	objects = UserManager()
