from django.db import models
# Import the reverse function
from django.urls import reverse

#Tuple to be called in any models up here:
TIMES = (
    ('M', 'Morning'),
    ('A', 'Afternoon'),
    ('E', 'Evening')
)

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

class Shouting(models.Model):
    date = models.DateField('Date shouted')
    time = models.CharField(
        max_length=1,
        choices=TIMES,
        default=TIMES[0][0]
    )
    #creating shout Foreign Key in Shouting
    shout = models.ForeignKey(Shout, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.get_time_display()} on {self.date}"
    
    # change the default sorting
    class Meta:
        ordering = ['-date']