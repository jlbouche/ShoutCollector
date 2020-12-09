from django.shortcuts import render

from django.http import HttpResponse

#temporary place for Shouts class/model

class Shout:  # Note that parens are optional if not inheriting from another class
  def __init__(self, name, words, translation, effect):
    self.name = name
    self.words = words
    self.translation = translation
    self.effect = effect

shouts = [
  Shout('Unrelenting Force', 'Fus Ro Dah', 'Force Balance Push', 'Your Voice is raw power, pushing aside anything - or anyone - who stands in your path'),
  Shout('Whirlwind Sprint', 'Wuld Nah Kest', 'Whirlwind Fury Tempest', 'The Thuum rushes forward, carrying you in its wake with the speed of a tempest'),
  Shout('Frost Breath', 'Fo Krah Diin', 'Frost Cold Freeze', 'Your breath is winter, your Thuum a blizzard')
]

# Create your views here.

def home(request):
    return HttpResponse('<h1>Hello</h1>')

def about(request):
    return render(request, 'about.html')

def shouts_index(request):
    return render(request, 'shouts/index.html', { 'shouts': shouts})