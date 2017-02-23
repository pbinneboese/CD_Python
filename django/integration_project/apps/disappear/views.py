from django.shortcuts import render, redirect

# Create your views here.
def index(request):
    return render(request, "disappear/index.html")

def ninjas(request, color):
    print "COLOR= ", color
    if (color == 'ninja'):
        image = 'disappear/img/tmnt.png'
    elif (color == 'blue'):
        image = 'disappear/img/leonardo.jpg'
    elif (color == 'orange'):
        image = 'disappear/img/michelangelo.jpg'
    elif (color == 'red'):
        image = 'disappear/img/raphael.jpg'
    elif (color == 'purple'):
        image = 'disappear/img/donatello.jpg'
    else:
        image = 'disappear/img/notapril.jpg'

    context = {
        'image': image
    }
    return render(request, "disappear/ninjas.html", context)
