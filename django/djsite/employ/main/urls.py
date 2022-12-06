from django.contrib import admin
from django.urls import path, include
from . import views
from .views import show_prog

urlpatterns = [

    path('', views.index, name="home"),
    path('prog/', views.prog, name="prog"),
    path('quest/', views.quest, name="quest"),
    path('reg/', views.reg, name="reg"),
    path('login/', views.login, name="login"),
    path('prog/<int:courses_id>/', show_prog, name='progs')

]
