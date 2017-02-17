from django.shortcuts import render, HttpResponse
# CONTROLLER - view
# Create your views here.
def index(request):
    # response = "Hello, I am your first request!"
    # return HttpResponse(response)
    return render(request, "first_app/index.html")
