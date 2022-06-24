from django.db import models

# Create your models here.

class Todo(models.Model):
    task = models.CharField(max_length=50, blank=False, default='')
    description = models.CharField(max_length=100, blank=False, default='')

    def __str__(self):
        return self.task
