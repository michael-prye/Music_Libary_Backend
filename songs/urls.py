import imp
from django.urls import path
from . import views

urlpatterns = [
    path('', views.all_songs),
    path('<int:pk>/', views.single_song)
    
]