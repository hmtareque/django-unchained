from django.shortcuts import render

# Create your views here.
from .models import Task

# Get tasks and display 
def index(request):
    return render(request, 'tasks/index.html')