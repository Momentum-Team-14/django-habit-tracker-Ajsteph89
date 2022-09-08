from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name="home"),
    path('habits/', views.list_habits, name='list_habits'),
    path('habit/add/', views.add_habit, name='add_habit'),
    path('habit_detail/<int:pk>', views.habit_detail, name='habit_detail'),
    path('record/new/<int:pk>', views.add_record, name='add_record'),
    path('habit/edit/<int:pk>', views.edit_habit, name='edit_habit'),
    path('delete_habit/<int:pk>', views.delete_habit, name='delete_habit'),
    path('record/edit/<int:pk1>/<int:pk2>', views.edit_record, name='edit_record'),
    path('delete_record/<int:pk1>/<int:pk2>', views.delete_record, name='delete_record'),
]