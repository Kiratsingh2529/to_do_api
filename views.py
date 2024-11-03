from rest_framework import generics
from .models import Todo
from .serializers import TodoSerializer
from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return HttpResponse("<h1>Welcome to the To-Do List API</h1><p>Use the /api/todos/ endpoint to manage your tasks.</p>")


class TodoListCreateAPIView(generics.ListCreateAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer

class TodoRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Todo.objects.all()
    serializer_class = TodoSerializer





def home(request):
    todos = Todo.objects.all()  # Get all todo items
    return render(request, 'todos/todo_list.html', {'todos': todos})  # Pass todos to the template
