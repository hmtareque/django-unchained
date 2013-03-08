from django.contrib import admin

# Register your models here.
from .models import Task

admin.site.site_header = 'Todo App'
admin.site.site_title = 'Todo App Admin'
admin.site.index_title = 'Welcome to Todo App'

class TaskAdmin(admin.ModelAdmin):
    fields = ['task', 'created_at']
    list_display = ('task', 'created_at', 'completed_at')

admin.site.register(Task, TaskAdmin)