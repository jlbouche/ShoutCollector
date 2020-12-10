from django.urls import path # path helps us define a route
from . import views # views = controller functions
# . import everything

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('shouts/', views.shouts_index, name='index'),
    path('shouts/<int:shout_id>/', views.shouts_detail, name='detail'),
    # new route used to show a form and create a cat
    path('shouts/create/', views.ShoutCreate.as_view(), name='shouts_create'),
    path('shouts/<int:pk>/update/', views.ShoutUpdate.as_view(), name='shouts_update'),
    path('shouts/<int:pk>/delete/', views.ShoutDelete.as_view(), name='shouts_delete'),
]