from django.db import models

class Task(models.Model):
  name = models.CharField(max_length=255)
  description = models.TextField()
  done_at = models.DateTimeField(null=True, blank=True)
