from urllib import response
from rest_framework import viewsets
from .serailizers import TaskSerializer
from .models import Todo
from django.http import JsonResponse


# Create your views here.
class TodoAPIView(viewsets.ModelViewSet):
    queryset = Todo.objects.all()
    print(queryset)
    serializer_class = TaskSerializer