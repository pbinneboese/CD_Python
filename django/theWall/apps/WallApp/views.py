from django.shortcuts import render, redirect
from django.contrib import messages
from .models import User, Message, Comment

# Create your views here.
def index(request):
	return render(request, "WallApp/index.html")

def register(request):    # process user registration form
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
	print request.session
	if not 'user_id' in request.session:
		messages.error(request, "Not logged in, please login or register")
		return redirect("WallApp:index")
	else:
		messages = Message.objects.show_messages(user_id=request.session['user_id'])
		comments = Comment.objects.show_comments(user_id=request.session['user_id'])
		return render(request, "WallApp/success.html", messages, comments)

def logout(request):    # process user logout form
	if request.method == "POST":
		request.session.clear()
	return redirect("WallApp:index")

def create_message(request):

    # get the current_time by importing the datetime module
    current_time = datetime.datetime.now()
    for message in messages:
        # get the difference between the current time and the time the message was created and save to the db
        difference = current_time - message['created_at']
        # convert the difference to a string in order to do the comparsion,  both datetime.now() and the NOW() has a data type of datetime, can not perform comparsion without a conversion first
        difference = str(difference)
        # if the difference is under 30 mins:
        if difference < '0:30:00':
            # add true to the query object
            message['can_delete'] = True
        else:
            # else add false
            message['can_delete'] = False

    return redirect('/success')

def create_comment(request):
    return redirect('/success')

def delete_message(request):
    return redirect('/success')
