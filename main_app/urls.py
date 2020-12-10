from django.urls import path # path helps us define a route
from . import views # views = controller functions
# . import everything

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('shouts/', views.shouts_index, name='index'),
    path('shouts/<int:shout_id>/', views.shouts_detail, name='detail'),
]