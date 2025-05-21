from django.urls import path
from .views import (
    TaskCreateView,
    TaskListView,
    TaskDeleteView,
    UserCreateView,
    BoardCreateView,
    SprintCreateView,
    ColumnCreateView,
    GroupCreateView,
)

urlpatterns = [
    path('api/tasks/', TaskListView.as_view(), name='task-list'),
    path('api/tasks/create/', TaskCreateView.as_view(), name='task-create'),
    path('api/tasks/<int:task_id>/', TaskDeleteView.as_view(), name='task-delete'),
    path('api/users/', UserCreateView.as_view(), name='user-create'),
    path('api/groups/', GroupCreateView.as_view(), name='group-create'),
    path('api/boards/', BoardCreateView.as_view(), name='board-create'),
    path('api/columns/', ColumnCreateView.as_view(), name='column-create'),
    path('api/sprints/', SprintCreateView.as_view(), name='sprint-create'),
]