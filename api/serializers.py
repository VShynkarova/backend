from rest_framework import serializers
from .models import Task


class TaskSerializer(serializers.ModelSerializer):  # TODO
    """ map Task model instalce into JSON format """
    details = serializers.CharField(required=False, allow_blank=True)

    class Meta:
        """ map serializer's fields with model fields """
        model = Task
        fields = '__all__'
        read_only_fields = ('date_created',)
