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

def result(request):
    return render(request, "surveyApp/result.html")

def process(request):
    if request.method == "POST":
        request.session['times'] = request.session['times'] + 1
        request.session['name'] = request.POST['name']
        request.session['dojo_location'] = request.POST['dojo_location']
        request.session['favorite_language'] = request.POST['favorite_language']
        request.session['comment'] = request.POST['comment']
        print "SESSION= ", request.session
        return redirect("surveyApp:result")
        # context = {
        #     'name': request.POST['name'],
        #     'dojo_location': request.POST['dojo_location'],
        #     'favorite_language': request.POST['favorite_language'],
        #     'comment': request.POST['comment']
        # }
        # print "CONTEXT= ", context
        # return redirect("/result", context)
    else:
        return redirect("surveyApp:index")
