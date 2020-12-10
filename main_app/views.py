from django.shortcuts import render
# Add the following import
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Shout

# Create your views here.

#Create, Update, and Delete view functions:

class ShoutCreate(CreateView):
  model = Shout
  fields = '__all__'
  success_url = '/shouts/'

class ShoutUpdate(UpdateView):
  model = Shout
  # Let's disallow the renaming of a cat by excluding the name field!
  fields = ['translation', 'name', 'effect']

class ShoutDelete(DeleteView):
  model = Shout
  success_url = '/shouts/'

#url view formats

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