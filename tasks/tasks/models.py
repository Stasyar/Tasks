from django.db import models


class TaskStatus(models.TextChoices):
    TODO = 'todo'
    IN_PROGRESS = 'in_progress'
    DONE = 'done'


class User(models.Model):
    full_name = models.CharField(max_length=100, null=False)
    email = models.CharField(max_length=120, null=False)
    created_at = models.DateTimeField(null=False, auto_now_add=True)


class Task(models.Model):
    title = models.CharField(max_length=255, null=False)
    description = models.TextField(null=True)
    status = models.CharField(max_length=20, choices=TaskStatus.choices, default=TaskStatus.TODO)
    created_at = models.DateTimeField(null=False, auto_now_add=True)
    author = models.ForeignKey("User", on_delete=models.CASCADE, null=False, related_name="tasks")
    assignee = models.ForeignKey("User", on_delete=models.SET_NULL, null=True, blank=True,
                                 related_name="assigned_tasks")

    board_id = models.IntegerField(null=True, blank=True)
    column_id = models.IntegerField(null=True, blank=True)
    sprint_id = models.IntegerField(null=True, blank=True)
    group_id = models.IntegerField(null=True, blank=True)

    executors = models.ManyToManyField("User", related_name="executed_tasks", blank=True)
    watchers = models.ManyToManyField("User", related_name="watched_tasks", blank=True)
