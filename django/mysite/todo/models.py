from django.db import models

class Todo(models.Model):
   text = models.CharField(max_length=100)
   deadline = models.DateField(auto_now=True)
