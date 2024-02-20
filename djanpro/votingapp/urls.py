from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    # path('subv', views.subvot, name='subvot')
    path('getquery',views.getquery, name='getquery'),
    path('reset', views.reset, name='reset'),
    path('sortd', views.sortd, name='sortd'),
    path('results', views.result, name='results')
    
]