from django.shortcuts import render, redirect
from .models import Course

# Create your views here.
def index(request):
    context = {
        "courses": Course.objects.all()
    }
    return render(request, "theApp/index.html", context)

def create(request):    # process course creation form
    if request.method == "POST":
        Course.objects.create(name=request.POST['name'], description=request.POST['description'])
    return redirect("/")

def destroy(request, id):   # prompt for course deletion
    course = Course.objects.get(id=id)
    context = {
        "course": course
    }
    return render(request, "theApp/destroy.html", context)

def delete(request):    # process course deletion form
    if request.method == "POST":
        print "ID= ", request.POST['id']
        if request.POST['response'] == "Yes":
            course = Course.objects.get(id=request.POST['id'])
            course.delete()
    return redirect("/")
