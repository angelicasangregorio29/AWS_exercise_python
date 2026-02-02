from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    bio = models.TextField(blank=True)
    linkedin_url = models.URLField(blank=True)

    matricola = models.OneToOneField(
        'matricola.Matricola',
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='user',
    )

    def __str__(self):
        return self.username
