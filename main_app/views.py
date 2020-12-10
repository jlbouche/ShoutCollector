from django.shortcuts import render

from .models import Shout

from django.http import HttpResponse

# Create your views here.
def home(request):
    return render(request, 'home.html') # res.send

def about(request):
    return render(request, 'about.html')

def shouts_index(request):
    # use our model to get all the cats
    shouts = Shout.objects.all()
    #injecting variable called 'cats' with value cats
    return render(request, 'shouts/index.html', {'shouts': shouts}) 

def shouts_detail(request, shout_id):
    #find the cat that has the id of cat_id
    shout = Shout.objects.get(id=shout_id)
    return render(request, 'shouts/detail.html', {'shout': shout})