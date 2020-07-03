from datetime import datetime
from django.db import models

# Create your models here.
class Event(models.Model):
    
    title = models.CharField(max_length=255)
    description = models.TextField()
    date = models.DateTimeField(default=datetime.now)
    is_done = models.BooleanField()
    thumbnail = models.ImageField(upload_to='event_thumbnails/')

    def __str__(self):
        return self.title