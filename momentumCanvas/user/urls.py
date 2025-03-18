from django.contrib import admin
from django.urls import path
from .import views
urlpatterns = [
    path("", views.home, name="home"),
    path('signUp', views.signUp, name='signUp'),
    path('dashboard', views.dashboard, name="dashboard"),
    path('signIn', views.signIn, name='signIn'),
    path('platformDetail/<str:platformName>/', views.platformDetail, name="platformDetail"),
    path('error', views.error, name='error'),
    path('analytics', views.analytics, name='analytics'),
]