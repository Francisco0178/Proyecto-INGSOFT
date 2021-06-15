from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='embarques-home'),
    path('about/', views.about, name='embarques-about'),
]