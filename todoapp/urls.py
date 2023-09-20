from django.urls import path
from . import views
from .api_views import TaskCreateAPIView, TaskRetrieveAPIView, TaskListAPIView, TaskUpdateAPIView, TaskDeleteAPIView

urlpatterns = [
    path('', views.task_list, name='task_list'),
    path('task/create/', views.task_create, name='task_create'),
    path('task/<int:task_id>/', views.task_detail, name='task_detail'),
    path('task/<int:task_id>/update/', views.task_update, name='task_update'),
    path('task/<int:task_id>/delete/', views.task_delete, name='task_delete'),
    path('api/tasks/', TaskListAPIView.as_view(), name='api-task-list'),
    path('api/tasks/create/', TaskCreateAPIView.as_view(), name='api-task-create'),
    path('api/tasks/<int:pk>/', TaskRetrieveAPIView.as_view(), name='api-task-retrieve'),
    path('api/tasks/<int:pk>/update/', TaskUpdateAPIView.as_view(), name='api-task-update'),
    path('api/tasks/<int:pk>/delete/', TaskDeleteAPIView.as_view(), name='api-task-delete'),
]
