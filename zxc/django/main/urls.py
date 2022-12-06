from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [

    path('', views.index, name="home"),
    path('prog/', views.prog, name="prog"),
    path('quest/', views.quest, name="quest")


]