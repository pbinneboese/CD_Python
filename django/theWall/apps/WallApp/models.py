from __future__ import unicode_literals

from django.db import models
import bcrypt
import re

EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
NAME_REGEX = re.compile(r'^[a-zA-Z][a-zA-Z]+$')

# Create your models Managers here.
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
			return {'status':False, 'errors':errors}
		else:  # Successfully Registered
			# encrypt password
			password = str(postData['password'])
			hashed_pw = bcrypt.hashpw(password, bcrypt.gensalt())
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
			return {'status':False, 'errors':errors}
		else:  # Successfully Logged In
			print "LOGGED IN= ", this_user.id
			return {'status':True, 'user':this_user}

class MessageManager(models.Manager):
	def show_messages(self, postData):  # for showing all messages by this user
		errors = []
		messages = self.filter(user=postData['user_id'])
		if errors:
			return {'status':False, 'errors':errors}
		else:
			return {'status':True, 'messages':messages}

	def create_message(self, postData):  # for creating a new message
		errors = []
		user = User.objects.get(id=postData['user_id'])
		message = self.create(content=postData['content'], user=user)
		if errors:
			return {'status':False, 'errors':errors}
		else:
			return {'status':True, 'message':message}

	def delete_message(self, postData):  # for deleting a message
		errors = []
		message = self.get(id=postData['message_id'])
		message.delete()
		if errors:
			return {'status':False, 'errors':errors}
		else:
			return {'status':True, 'message':message}

class CommentManager(models.Manager):
	def show_comments(self, postData):  # for showing all comments by this user
		errors = []
		comments = self.filter(user=postData['user_id'])
		if errors:
			return {'status':False, 'errors':errors}
		else:
			return {'status':True, 'comments':comments}

	def create_comment(self, postData):  # for creating a new comment
		errors = []
		message = Message.objects.get(id=postData['message_id'])
		user = User.objects.get(id=postData['user_id'])
		comment = self.create(content=postData['content'], message=message, user=user)
		if errors:
			return {'status':False, 'errors':errors}
		else:
			return {'status':True, 'comment':comment}

	def delete_comment(self, postData):  # for deleting a comment
		errors = []
		comment = self.get(id=postData['comment_id'])
		comment.delete()
		if errors:
			return {'status':False, 'errors':errors}
		else:
			return {'status':True, 'comment':comment}

# Create your models here.
class User(models.Model):
	first_name = models.CharField(max_length=255)
	last_name = models.CharField(max_length=255)
	email = models.EmailField()
	password = models.CharField(max_length=255)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)
	objects = UserManager()

class Message(models.Model):
	content = models.TextField()
	user = models.ForeignKey(User, related_name='messages_user')
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)
	objects = MessageManager()

class Comment(models.Model):
	content = models.TextField()
	message = models.ForeignKey(Message, related_name = 'comments_msg')
	user = models.ForeignKey(User, related_name = 'comments_user')
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)
	objects = CommentManager()
