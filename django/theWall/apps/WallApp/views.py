from django.shortcuts import render, redirect
from django.contrib import messages
from .models import User, Message, Comment
# import arrow

# Create your views here.
def index(request):
	return render(request, "WallApp/index.html")

def register(request):    # process user registration form
	print "REGISTER"
	if request.method == "POST":
		response = User.objects.register(request.POST)
		if response['status'] == False:
			for error in response['errors']:
				messages.error(request, error)
			return redirect("WallApp:index")
		else:
			# password is validated, save user_id for session
			this_user = response['user']
			print "THIS USER ", this_user.id
			request.session['user_id'] = this_user.id
			request.session['first_name'] = this_user.first_name
			return redirect("WallApp:success")
	else:
		return redirect("WallApp:index")

def login(request):    # process user login form
	print "LOGIN"
	if request.method == "POST":
		response = User.objects.login(request.POST)
		if response['status'] == False:
			for error in response['errors']:
				messages.error(request, error)
			return redirect("WallApp:index")
		else:
			# password is validated, save user_id for session
			this_user = response['user']
			print "THIS USER ", this_user.id
			request.session['user_id'] = this_user.id
			request.session['first_name'] = this_user.first_name
			return redirect("WallApp:success")
	else:
		return redirect("WallApp:index")

def success(request):
	print "SUCCESS"
	# print request.session
	if not 'user_id' in request.session:
		messages.error(request, "Not logged in, please login or register")
		return redirect("WallApp:index")
	else:
		context = {
			'messages': Message.objects.all(),
			'comments': Comment.objects.all()
		}
		# messages = Message.objects.show_messages(request.session)
		# comments = Comment.objects.show_comments(request.session)
		return render(request, "WallApp/success.html", context)

def logout(request):    # process user logout form
	print "LOGOUT"
	if request.method == "POST":
		request.session.clear()
	return redirect("WallApp:index")

def create_message(request):
	print "CREATE_MESSAGE"
	if request.method == "POST":
		context = {
			'content': request.POST['content'],
			'user_id': request.session['user_id']
		}
		Message.objects.create_message(context)
	else:
		return redirect("WallApp:success")

	# walk the list of this user's messages, see which ones are <30 minutes old, and flag them as potentially delete-able
	# first, get the current_time
	# current_time = arrow.utcnow()
	# response = Message.objects.show_messages(request.session)
	# if response['status'] == False:
	# 	return redirect("WallApp:success")
	# for message in response['messages']:
	# 	# get the difference between the current time and the time the message was created and save to the db
	# 	difference = current_time - message.created_at
	# 	difference = str(difference)  # convert to string for comparison
	# 	print difference
	# 	if the difference is under 30 mins:
	# 	if difference < '0:30:00':
	# 		message['can_delete'] = True
	# 	else:
	# 		message['can_delete'] = False
	return redirect("WallApp:success")

def create_comment(request, message_id):
	print "CREATE_COMMENT", message_id
	if request.method == "POST":
		context = {
			'content': request.POST['content'],
			'message_id': message_id,
			'user_id': request.session['user_id']
		}
		response = Comment.objects.create_comment(context)
	return redirect("WallApp:success")

def delete_message(request, message_id):
	print "DELETE_MESSAGE", message_id
	if request.method == "POST":
		context = {
			'message_id': message_id
		}
		response = Message.objects.delete_message(context)
	return redirect("WallApp:success")

def delete_comment(request, comment_id):
	print "DELETE_COMMENT", comment_id
	if request.method == "POST":
		context = {
			'comment_id': comment_id
		}
		response = Comments.objects.delete_comment(context)
	return redirect("WallApp:success")
