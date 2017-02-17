from django.shortcuts import render, HttpResponse
import datetime

# Create your views here.
def index(request):
    context = {
        "somekey":datetime.datetime.now()
        # "somekey":"123456"
    }
    return render(request, "timedisplay/index.html", context)
