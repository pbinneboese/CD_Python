from django.shortcuts import render, HttpResponse, redirect

# Create your views here.
def check_init(request):
    if 'times' in request.session:
        print 'True'
    else:
        request.session['times'] = 0
        print 'False'

def index(request):
    check_init(request)
    return render(request, "surveyApp/index.html")

def result(request, context):
    return render(request, "surveyApp/result.html", context)

def process(request):
    if request.method == "POST":
        print "REQUEST= ", request.POST
        context = {
            'name': request.POST['name'],
            'dojo_location': request.POST['dojo_location'],
            'favorite_language': request.POST['favorite_language'],
            'comment': request.POST['comment']
        }
        print "CONTEXT= ", context
        request.session['times'] = request.session['times'] + 1
        return redirect("/result", context)
    else:
        return redirect("/")
