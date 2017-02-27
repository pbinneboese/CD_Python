from __future__ import unicode_literals

from django.core.exceptions import ObjectDoesNotExist
from django.db import models
from ..loginReg.models import User

# Create your models Managers here.
class MessageManager(models.Manager):
	def show_messages(self, postData):  # for showing all messages by this user
		messages = self.filter(user=postData['user_id'])
		return {'status':True, 'messages':messages}

	def create_message(self, postData):  # for creating a new message
		try:	# check if user exists
			user = User.objects.get(id=postData['user_id'])
		except ObjectDoesNotExist:
			return {'status':False}
		message = self.create(content=postData['content'], user=user)
		return {'status':True, 'message':message}

	def delete_message(self, postData):  # for deleting a message
		try:	# check if message exists
			message = self.get(id=postData['message_id'])
		except ObjectDoesNotExist:
			return {'status':False}
		message.delete()
		return {'status':True}

class LikeManager(models.Manager):
	def show_likes(self, postData):  # for showing all likes by this user
		likes = self.filter(user=postData['user_id'])
		return {'status':True, 'likes':likes}

	def create_like(self, postData):  # for creating a new like
		try:# check if message exists
			message = Message.objects.get(id=postData['message_id'])
		except ObjectDoesNotExist:
			return {'status':False}
		try:# check if user exists
			user = User.objects.get(id=postData['user_id'])
		except ObjectDoesNotExist:
			return {'status':False}
		try:	# don't create duplicate likes
			like = self.get(message=message, user=user)
		except ObjectDoesNotExist:
			message.likes += 1;
			message.save()
			like = self.create(message=message, user=user)
			return {'status':True, 'like':like}
		else:
			return {'status':False}

	def delete_like(self, postData):  # for deleting a like
		try:	# check if like exists
			like = self.get(id=postData['like_id'])
		except ObjectDoesNotExist:
			return {'status':False}
		try:	# check if message exists
			message = Message.objects.get(id=like.message.id)
		except ObjectDoesNotExist:
			return {'status':False}
		message.likes -= 1;
		message.save()
		like.delete()
		return {'status':True}

# class CommentManager(models.Manager):
# 	def show_comments(self, postData):  # for showing all comments by this user
# 		comments = self.filter(user=postData['user_id'])
# 		if not comments.exists():
# 			return {'status':False}
# 		else:
# 			return {'status':True, 'comments':comments}
#
# 	def create_comment(self, postData):  # for creating a new comment
# 		message = Message.objects.get(id=postData['message_id'])
# 		if not message.exists():
# 			return {'status':False}
# 		user = User.objects.get(id=postData['user_id'])
# 		if not user.exists():
# 			return {'status':False}
# 		comment = self.create(content=postData['content'], message=message, user=user)
# 		return {'status':True, 'comment':comment}
#
# 	def delete_comment(self, postData):  # for deleting a comment
# 		comment = self.get(id=postData['comment_id'])
# 		if not comment.exists():
# 			return {'status':False}
# 		comment.delete()
# 		return {'status':True}

# Create your models here.
class Message(models.Model):
	likes = models.IntegerField(default=0)
	content = models.TextField()
	user = models.ForeignKey(User, related_name='messages_user')
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)
	objects = MessageManager()

class Like(models.Model):
	message = models.ForeignKey(Message, related_name = 'likes_message')
	user = models.ForeignKey(User, related_name = 'likes_user')
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)
	objects = LikeManager()

# class Comment(models.Model):
# 	content = models.TextField()
# 	message = models.ForeignKey(Message, related_name = 'comments_msg')
# 	user = models.ForeignKey(User, related_name = 'comments_user')
# 	created_at = models.DateTimeField(auto_now_add=True)
# 	updated_at = models.DateTimeField(auto_now=True)
# 	objects = CommentManager()
