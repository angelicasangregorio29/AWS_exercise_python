import uuid
from django.db import models

class Pokemon(models.Model):
    # Core Identity (Unique per instance)
    id = models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True)
    
    # Species Data (Shared by many instances)
    name = models.CharField(max_length=200) # e.g. "Snorlax"
    pokedex_id = models.IntegerField() # e.g. 143
    
    # Individual Stats (Varies per instance)
    level = models.IntegerField(default=1)
    type_primary = models.CharField(max_length=50, default="Normal")
    type_secondary = models.CharField(max_length=50, null=True, blank=True)
    
    # Unique Property (Example of non-duplicate field)
    # Let's say each Pokemon caught has a unique registration serial number from the capture ball
    capture_id = models.CharField(max_length=50, unique=True, help_text="Unique ID from the capture device")
    
    is_shiny = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} (Lvl {self.level})"
