from django.forms import ModelForm
from .models import Shouting

class ShoutingForm(ModelForm):
  class Meta:
    model = Shouting
    fields = ['date', 'time']