from django.db import models

# Create your models here.
class Task(models.Model):
    task = models.CharField(max_length=200)
    created_at = models.DateTimeField()
    completed_at = models.DateTimeField(null=True)
