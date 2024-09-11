# tasks/urls.py

from django.urls import path
from . import views

urlpatterns = [
    path('add/', views.add_task, name='add_task'),
    path('edit/<int:id>/', views.edit_task, name='edit_task'),
    path('delete/<int:id>/', views.delete_task, name='delete_task'),
    path('filter/<str:priority>/', views.filter_tasks_by_priority, name='filter_tasks_by_priority'),
    path('', views.view_all_tasks, name='view_all_tasks'),
]
