from django.urls import path
from . import views

urlpatterns = [
     path('task/', views.task_view, name='task'),
     path('task/create/', views.create_task_view, name='createtask'),
     path('task/update/<int:task_id>/', views.task_update, name='update_task'),
     path('stats/', views.statistics_view, name='stats'),
     path('profile/', views.profile_view, name='profile'),
     path('profile/update/', views.update_profile_view, name='update_profile'),
]
