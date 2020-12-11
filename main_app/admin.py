from django.contrib import admin
#import models here
from .models import Shout, Shouting
# Register your models here.
admin.site.register(Shout)
admin.site.register(Shouting)