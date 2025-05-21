import logging

from rest_framework import generics
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.exceptions import APIException
from .models import Task, User, Column, Board, Sprint, Group
from .serializers import (
    TaskSerializer,
    UserSerializer,
    GroupSerializer,
    ColumnSerializer,
    SprintSerializer, BoardSerializer
)

logger = logging.getLogger(__name__)

class UserCreateView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer

    def perform_create(self, serializer):
        try:
            user = serializer.save()
            logger.info(f"User created: {user}")
        except Exception as e:
            logger.error(f"Error during creating user: {e}")
            raise APIException("User was not created")


class TaskCreateView(generics.CreateAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

    def perform_create(self, serializer):
        try:
            task = serializer.save()
            logger.info(f"Task created: {task}")
        except Exception as e:
            logger.error(f"Error during creating task: {e}")
            raise APIException("Task was not created")


class TaskListView(generics.ListAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['status', 'author', 'assignee', 'board_id', 'sprint_id']
    pagination_class = None

    def get_queryset(self):
        try:
            queryset = super().get_queryset()
            logger.info("Tasks list was received")
            return queryset
        except Exception as e:
            logger.error(f"Error during getting tasks list: {e}")
            raise APIException("Tasks list was not received")


class TaskDeleteView(generics.DestroyAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer
    lookup_url_kwarg = 'task_id'

    def delete(self, request, *args, **kwargs):
        try:
            response = super().delete(request, *args, **kwargs)
            logger.info(f"Task: ID {kwargs.get('task_id')} was deleted")
            return response
        except Exception as e:
            logger.error(f"Error during deleting task: {e}")
            raise APIException("Task was not deleted")


class ColumnCreateView(generics.CreateAPIView):
    queryset = Column.objects.all()
    serializer_class = ColumnSerializer

    def perform_create(self, serializer):
        try:
            column = serializer.save()
            logger.info(f"Column created: {column}")
        except Exception as e:
            logger.error(f"Error during creating column: {e}")
            raise APIException("Column was not created")


class SprintCreateView(generics.CreateAPIView):
    queryset = Sprint.objects.all()
    serializer_class = SprintSerializer

    def perform_create(self, serializer):
        try:
            sprint = serializer.save()
            logger.info(f"Sprint created: {sprint}")
        except Exception as e:
            logger.error(f"Error during creating sprint: {e}")
            raise APIException("Sprint was not created")


class BoardCreateView(generics.CreateAPIView):
    queryset = Board.objects.all()
    serializer_class = BoardSerializer

    def perform_create(self, serializer):
        try:
            board = serializer.save()
            logger.info(f"Board created: {board}")
        except Exception as e:
            logger.error(f"Error during creating board: {e}")
            raise APIException("Board was not created")


class GroupCreateView(generics.CreateAPIView):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer

    def perform_create(self, serializer):
        try:
            group = serializer.save()
            logger.info(f"Group created: {group}")
        except Exception as e:
            logger.error(f"Error during creating group: {e}")
            raise APIException("Group was not created")
