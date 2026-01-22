from django.db import models

# Create your models here.

class Project(models.Model):
    title = models.CharField(max_length=200)

    def __str__(self):
        return self.title

class Task(models.Model):
    description = models.CharField(max_length=200)
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name='tasks')

    def __str__(self):
        return self.description