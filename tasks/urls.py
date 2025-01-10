# tasks/urls.py
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('add/', views.add_task, name='add_task'),
    path('mark_completed/<int:id>/', views.mark_completed, name='mark_completed'),
    path('delete/<int:id>/', views.delete_task, name='delete_task'),
]
