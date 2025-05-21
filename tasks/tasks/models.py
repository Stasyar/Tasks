from django.conf import settings
from django.contrib.auth import get_user_model
from django.contrib.auth.models import AbstractUser
from django.db import models


class TaskStatus(models.TextChoices):
    TODO = 'todo'
    IN_PROGRESS = 'in_progress'
    DONE = 'done'


class CustomUser(AbstractUser):
    created_at = models.DateTimeField(auto_now_add=True)


User = get_user_model()


class Board(models.Model):
    name = models.CharField(max_length=100, unique=True)


class Column(models.Model):
    name = models.CharField(max_length=100)
    board = models.ForeignKey(Board, on_delete=models.CASCADE, related_name='columns')


class Sprint(models.Model):
    name = models.CharField(max_length=100)
    start_date = models.DateField(null=True, blank=True)
    end_date = models.DateField(null=True, blank=True)


class Group(models.Model):
    name = models.CharField(max_length=100, unique=True)


class Task(models.Model):
    title = models.CharField(max_length=255, null=False)
    description = models.TextField(null=True)
    status = models.CharField(max_length=20, choices=TaskStatus.choices, default=TaskStatus.TODO)
    created_at = models.DateTimeField(null=False, auto_now_add=True)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=False, related_name="tasks")
    assignee = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, blank=True,
                                 related_name="assigned_tasks")

    column = models.ForeignKey(Column, on_delete=models.CASCADE, null=True, blank=True)
    sprint = models.ForeignKey(Sprint, on_delete=models.CASCADE, null=True, blank=True)
    board = models.ForeignKey(Board, on_delete=models.CASCADE, null=True, blank=True)
    group = models.ForeignKey(Group, on_delete=models.CASCADE, null=True, blank=True)

    executors = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name="executed_tasks", blank=True)
    watchers = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name="watched_tasks", blank=True)
