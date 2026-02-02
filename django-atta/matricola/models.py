from django.db import models
import uuid

class Matricola(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    matricola = models.CharField(max_length=50, unique=True)

    def __str__(self):
        return f"{self.matricola}"

    class Meta:
        db_table = "matricole"