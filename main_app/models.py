from django.db import models
# Import the reverse function
from django.urls import reverse

# Create your models here.
class Shout(models.Model):
    words = models.CharField(max_length=100)
    translation = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    effect = models.TextField(max_length=250)

    def __str__(self):
        return self.words
    
    def get_absolute_url(self):
        return reverse('detail', kwargs={'shout_id': self.id})