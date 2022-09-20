from django.db import models

# Create your models here.
class Todos(models.Model):
    content= models.TextField(max_length=250, null=True, blank=True)