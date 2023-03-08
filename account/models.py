from django.db import models

# Create your models here.

class Comment(models.Model):
    name=models.CharField(max_length=50)
    email=models.EmailField(max_length=50)
    comment=models.TextField()
    date=models.DateTimeField(auto_now_add=True)

class Update(models.Model):
    name=models.CharField(max_length=50)
    email=models.EmailField(max_length=50)
