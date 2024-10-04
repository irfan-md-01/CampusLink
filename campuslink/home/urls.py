from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    # path('home/', views.home, name='members'),
    path('', views.index, name='index'),
    path('login/', views.login, name='login'),
    path('regist/', views.regist, name='regist'),
    path('register/', views.register, name='register'),
    path('UserDashboard/', views.UserDashboard, name='UserDashboard'),
    path('events/', views.events, name='events'),
]