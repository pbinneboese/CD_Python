from django.shortcuts import render, HttpResponse, redirect
import random, string

# Create your views here.
def check_init(request):
    if 'times' in request.session:
        print 'True'
    else:
        request.session['times'] = 0
        times = 0
        random_word = ""
        print 'False'

def index(request):
    check_init(request)
    return render(request, "randomWord/index.html")

def create(request):
    if request.method == "POST":
        # print request.POST
        random_word = ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(14))
        request.session['times'] = request.session['times'] + 1
        request.session['random_word'] = random_word
        return redirect("/")
    else:
        return redirect("/")
