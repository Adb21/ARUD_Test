from rest_framework import serializers
from .models import Todo

class TaskSerializer(serializers.Serializer):
    class Meta :
        model = Todo
        fields = '__all__'
    