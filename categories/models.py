from django.db import models

# Create your models here.
class Category(models.Model):
    name=models.CharField(max_length=70)
    is_parent = models.BooleanField(default=0)
    parent_id = models.IntegerField(default=0)