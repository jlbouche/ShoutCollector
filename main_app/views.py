from django.shortcuts import render, redirect
# Add the following import
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.views.generic import ListView, DetailView
from .models import Shout, Dragon
#import Shouting form
from .forms import ShoutingForm

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
  shout = Shout.objects.get(id=shout_id)
  #get dragons not associated with shout
  dragons_shout_doesnt_have = Dragon.objects.exclude(id__in = shout.dragons.all().values_list('id'))
  # instantiate FeedingForm to be rendered in the template
  shouting_form = ShoutingForm()
  return render(request, 'shouts/detail.html', {
    # include the cat and feeding_form in the context
    'shout': shout, 'shouting_form': shouting_form,
    #add dragons to be displayed
    'dragons': dragons_shout_doesnt_have
  })

def add_shouting(request, shout_id):
  # create a ModelForm instance using the data in request.POST
  form = ShoutingForm(request.POST)
  # validate the form
  if form.is_valid():
    # don't save the form to the db until it
    # has the cat_id assigned
    new_shouting = form.save(commit=False)
    new_shouting.shout_id = shout_id
    new_shouting.save()
  return redirect('detail', shout_id=shout_id)

def assoc_dragon(request, shout_id, dragon_id):
  #get shout and add dragon to the shout
  Shout.objects.get(id=shout_id).dragons.add(dragon_id)
  #redirect back to detail page
  return redirect('detail', shout_id=shout_id)

def remove_dragon(request, shout_id, dragon_id):
  Shout.objects.get(id=shout_id).dragons.remove(dragon_id)
  return redirect('detail', shout_id=shout_id)

#views for M:M Dragons

class DragonList(ListView):
  model = Dragon

class DragonDetail(DetailView):
  model = Dragon

class DragonCreate(CreateView):
  model = Dragon
  fields = '__all__'

class DragonUpdate(UpdateView):
  model = Dragon
  fields = ['name', 'typeof']

class DragonDelete(DeleteView):
  model = Dragon
  success_url = '/dragons/'