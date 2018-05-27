from django.db import models

# Create your models here.
class Todo(models.Model):
	description = models.CharField(max_length=128)
	is_done = models.BooleanField(default=False)