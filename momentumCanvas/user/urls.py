from django.contrib import admin
from django.urls import path
from .import views
urlpatterns = [
    path("", views.home, name="home"),
    path('signUp', views.signUp, name='signUp'),
    path('dashboard', views.dashboard, name="dashboard"),
    path('signIn', views.signIn, name='signIn'),
     path('error', views.error, name='error'),
]