from django.shortcuts import render, redirect
from .models import Course
from ..loginReg.models import User

# Create your views here.
def index(request):
    context = {
        "the_courses": Course.objects.all()
    }
    return render(request, "courses/index.html", context)

def create(request):    # process course creation form
    if request.method == "POST":
        Course.objects.create(name=request.POST['name'], description=request.POST['description'])
    return redirect("courses:index")

def destroy(request, id):   # prompt for course deletion
    course = Course.objects.get(id=id)
    context = {
        "course": course
    }
    return render(request, "courses/destroy.html", context)

def delete(request):    # process course deletion form
    if request.method == "POST":
        print "ID= ", request.POST['id']
        if request.POST['response'] == "Yes":
            course = Course.objects.get(id=request.POST['id'])
            course.delete()
    return redirect("courses:index")

def roster(request):
    context = {
        "the_users": User.objects.all(),
        "the_courses": Course.objects.all()
    }
    return render(request, "courses/users_courses.html", context)

def add_user(request):    # process course creation form
    if request.method == "POST":
        user_id = request.POST['user_id']
        course_id = request.POST['course_id']
        print user_id, course_id
        if (user_id != "0" and course_id != "0"):  # validity check
            this_user = User.objects.get(id=user_id)
            this_course = Course.objects.get(id=course_id)
            this_course.users.add(this_user)
    return redirect("courses:roster")
