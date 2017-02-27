from django.shortcuts import render, redirect
from django.contrib import messages
from django.core.exceptions import ObjectDoesNotExist
from .models import Message, Like
from ..loginReg.models import User

# Create your views here.
def success(request):
	print "SUCCESS"
	# print request.session
	if not 'user_id' in request.session:
		messages.error(request, "Not logged in, please login or register")
		return redirect("loginReg:index")
	else:
		context = {
			'user_id': request.session['user_id']
		}
		user_likes = Like.objects.show_likes(context)
		context = {  # return 10 most recent messages
			'messages': Message.objects.order_by('-created_at')[:10],
			'user_likes': user_likes
		}
		return render(request, "secrets/success.html", context)
		# user = User.objects.get(id=request.session['user_id'])
		# context = {  # return 10 most recent messages
		# 	'messages': Message.objects.order_by('-created_at')[:10],
		# 	'user_likes': Like.objects.filter(user=user)
		# }
		# return render(request, "secrets/success.html", context)

def popular(request):
	print "POPULAR"
	# print request.session
	if not 'user_id' in request.session:
		messages.error(request, "Not logged in, please login or register")
		return redirect("loginReg:index")
	else:
		context = {
			'user_id': request.session['user_id']
		}
		user_likes = Like.objects.show_likes(context)
		context = {  # return 10 most recent messages
			'messages': Message.objects.order_by('-likes'),
			'user_likes': user_likes
		}
		return render(request, "secrets/popular.html", context)
		# user = User.objects.get(id=request.session['user_id'])
		# context = {  # return messages ordered by most likes
		# 	'messages': Message.objects.order_by('-likes'),
		# 	'user_likes': Like.objects.filter(user=user)
		# }
		# return render(request, "secrets/popular.html", context)

def create_message(request):
	print "CREATE_MESSAGE"
	if request.method != "POST":
		return redirect("secrets:success")
	context = {
		'content': request.POST['content'],
		'user_id': request.session['user_id']
	}
	response = Message.objects.create_message(context)
	if response['status']:
		print "Done"
	else:
		print "Failed"
	return redirect("secrets:success")

def create_like(request, message_id):
	print "CREATE_LIKE", message_id
	# if request.method != "POST":
	# 	return redirect("secrets:success")
	context = {
		'message_id': message_id,
		'user_id': request.session['user_id']
	}
	response = Like.objects.create_like(context)
	if response['status']:
		print "Done"
	else:
		print "Failed"
	return redirect("secrets:success")

def delete_message(request, message_id):
	print "DELETE_MESSAGE", message_id
	# if request.method != "POST":
	# 	return redirect("secrets:success")
	context = {
		'message_id': message_id
	}
	response = Message.objects.delete_message(context)
	if response['status']:
		print "Done"
	else:
		print "Failed"
	return redirect("secrets:success")

def delete_like(request, like_id):
	print "DELETE_LIKE", like_id
	# if request.method != "POST":
	# 	return redirect("secrets:success")
	context = {
		'like_id': like_id
	}
	response = Like.objects.delete_like(context)
	if response['status']:
		print "Done"
	else:
		print "Failed"
	return redirect("secrets:success")
