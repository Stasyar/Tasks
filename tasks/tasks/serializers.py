from rest_framework import serializers
from .models import User, Task, Board, Sprint, Group, Column


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'first_name', 'last_name', 'email', 'created_at']


class TaskSerializer(serializers.ModelSerializer):
    author = serializers.PrimaryKeyRelatedField(queryset=User.objects.all())
    assignee = serializers.PrimaryKeyRelatedField(queryset=User.objects.all(), allow_null=True, required=False)
    executors = serializers.PrimaryKeyRelatedField(many=True, queryset=User.objects.all(), required=False)
    watchers = serializers.PrimaryKeyRelatedField(many=True, queryset=User.objects.all(), required=False)

    class Meta:
        model = Task
        fields = [
            'id',
            'title',
            'description',
            'status',
            'created_at',
            'author',
            'assignee',
            'board',
            'column',
            'sprint',
            'group',
            'executors',
            'watchers',
        ]


class BoardSerializer(serializers.ModelSerializer):
    class Meta:
        model = Board
        fields = ['id', 'name']
        read_only_fields = ['id']


class SprintSerializer(serializers.ModelSerializer):
    class Meta:
        model = Sprint
        fields = ['id', 'name', 'start_date', 'end_date']
        read_only_fields = ['id']


class ColumnSerializer(serializers.ModelSerializer):
    class Meta:
        model = Column
        fields = ['id', 'name', 'board']
        read_only_fields = ['id']


class GroupSerializer(serializers.ModelSerializer):
    class Meta:
        model = Group
        fields = ['id', 'name']
        read_only_fields = ['id']