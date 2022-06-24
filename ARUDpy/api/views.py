from urllib import response
from rest_framework import generics
from .serailizers import TaskSerializer
from .models import Todo
from django.http import JsonResponse


# Create your views here.
class TodoAPIView(generics.ListAPIView):
    queryset = Todo.objects.all()
    print(queryset)
    serializer_class = TaskSerializer