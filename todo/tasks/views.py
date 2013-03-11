from django.contrib import messages
from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.utils import timezone
from django.contrib.auth.decorators import login_required

from .models import Task

# Create your views here.
from .models import Task

# Get tasks and display 
def index(request):
    tasks = Task.objects.filter(completed_at__isnull=True)
    context = {'tasks': tasks}
    return render(request, 'tasks/index.html', context)

# Create new task
@login_required(login_url='/admin/login')
def create(request):
    return render(request, 'tasks/create.html')

# Store a task
def store(request):
    if request.POST['task'].strip() == '':
        messages.error(request, "Please insert task")
        return redirect('/tasks/create')
    else:
        task = Task(task = request.POST['task'], created_at = timezone.now())
        task.save()
        return redirect('/tasks')

# Complete a task
def complete(request, task_id):
    task = Task.objects.get(pk=task_id)
    if task:
        task.completed_at = timezone.now()
        task.save()
        messages.success(request, "Task completed successfully")
        return redirect('/tasks')
    else:
        messages.error(request, "Failed to mark the task completed")
        return redirect('/tasks')