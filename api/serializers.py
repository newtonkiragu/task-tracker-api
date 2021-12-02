from rest_framework import serializers

from api.models import Tasks


class TasksSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tasks
        fields = ['id', 'text', 'day', 'reminder']
