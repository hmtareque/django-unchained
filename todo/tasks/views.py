from django.shortcuts import render
from django.http import HttpResponse 
from .models import Task

# Create your views here.
from .models import Task

# Get tasks and display 
def index(request):
    tasks = Task.objects.all()
    context = {'tasks': tasks}
    return render(request, 'tasks/index.html', context)

# Create new task
def create(request):
    return render(request, 'tasks/create.html')

# Store a task
def store(request):
    print('store task')
    

    return HttpResponse(request)

# Complete a task
def complete(request, task_id):
    return render(request, 'tasks/create.html')