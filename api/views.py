from rest_framework import generics
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status
from .serializers import TaskSerializer
from .models import Task

class TaskViewSet(viewsets.ModelViewSet):

    queryset = Task.objects.all()
    serializer_class = TaskSerializer

    def filter_queryset(self, queryset):
        queryset = super(TaskViewSet, self).filter_queryset(queryset)
        return queryset.order_by('id')

    # DELETE Tasks
    def delete(self, request, *args, **kwargs):
        for x in Task.objects.all().iterator(): x.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
