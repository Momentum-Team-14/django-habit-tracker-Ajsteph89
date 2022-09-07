from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('habits/', views.list_habits, name='list_habits'),
    path('habit/add/', views.add_habit, name='add_habit'),
]