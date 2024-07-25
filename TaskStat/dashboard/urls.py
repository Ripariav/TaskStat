from django.urls import path
from . import views

urlpatterns = [
     path('task/', views.task_view, name='task'),
     path('task/create', views.create_task_view, name='createtask'),
]
