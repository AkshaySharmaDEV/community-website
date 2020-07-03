from django.contrib import admin
from events import models as event_models

# Register your models here.
admin.site.register(event_models.Event)