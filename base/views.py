from django.http import HttpResponse
from django.shortcuts import render
from base.models import Todo

# Create your views here.

def home(request):
    todos = Todo.objects.all()
    context = {'todos': todos}
    print(todos)
    return render(request, 'index.html', context)

def create(request):
    return render(request, 'create.html')