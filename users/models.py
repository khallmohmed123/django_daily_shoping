from django.db import models

# Create your models here.
class User(models.Model):
    USER_ROLES = [
            ("A", "Admin"),
            ("N", "Normal"),
            ("T", "Trador"),
        ]
    name=models.CharField(max_length=70)
    created_date=models.DateField(auto_now_add=True)
    updated_date=models.DateField(auto_now=True)
    role=models.CharField(max_length=255,choices=USER_ROLES,default=USER_ROLES[1])
    email=models.CharField(max_length=225,unique = True)
    password=models.CharField(max_length=225)
    image=models.CharField(max_length=225,default=None, blank=True, null=True)

