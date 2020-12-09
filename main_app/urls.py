from django.urls import path #defines route
from .import views # views = controller functions
# . import everything

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('shouts/', views.shouts_index, name='index'),
]