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
    path('shouts/<int:shout_id>/add_shouting/', views.add_shouting, name='add_shouting'),
    #associate dragon with shout (M:M)
    path('shouts/<int:shout_id>/assoc_dragon/<int:dragon_id>/', views.assoc_dragon, name='assoc_dragon'),
    path('/dragons/', views.DragonList.as_view(), name='dragons_index'),
    path('dragons/<int:pk>/', views.DragonDetail.as_view(), name='dragons_detail'),
    path('dragons/create/', views.DragonCreate.as_view(), name='dragons_create'),
    path('dragons/<int:pk>/update', views.DragonUpdate.as_view(), name='dragons_update'),
    path('dragons/<int:pk>/delete/', views.DragonDelete.as_view(), name='dragons_delete'),
]