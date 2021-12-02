from django.shortcuts import render, get_object_or_404

# Create your views here.
from rest_framework import viewsets, status
from rest_framework.response import Response

from api.models import Tasks
from api.serializers import TasksSerializer


class TasksViewSet(viewsets.ViewSet):
    """
    Tasks Viewset to display a list of tasks.
    Can perform GET and POST
    """

    def list(self, request):
        queryset = Tasks.objects.all()
        serializer = TasksSerializer(queryset, many=True)
        return Response(serializer.data)

    def create(self, request):
        print(request.data)
        data = request.data
        serializer = TasksSerializer(data=data)
        if not serializer.is_valid():
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        tasks_model = Tasks(**serializer.data)
        tasks_model.save()
        return Response({'tasks': serializer.data})

    def retrieve(self, request, pk=None):
        queryset = Tasks.objects.all()
        tasks = get_object_or_404(queryset, pk=pk)
        serializer = TasksSerializer(tasks)
        return Response(serializer.data)
