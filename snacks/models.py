from django.db import models
from django.contrib.auth import get_user_model
from django.db.models.deletion import CASCADE
from django.db.models.fields import TextField
from django.db.models.fields.related import ForeignKey
# Create your models here.

class Snack(models.Model):
    name = models.CharField(max_length=64)
    purchaser = models.ForeignKey(on_delete=models.CASCADE)
    description = models.TextField

def __str__(self):
    return self.name
