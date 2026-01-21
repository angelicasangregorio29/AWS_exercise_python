from django.db import models

# Create your models here.

class Project(models.Model):
    title = models.CharField(max_length=200)
    is_available = models.BooleanField(default=False)