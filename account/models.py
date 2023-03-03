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

class Image1(models.Model):
    image1=models.ImageField(upload_to='images/', blank=True, null=True)

class Image2(models.Model):
    image2=models.ImageField(upload_to='images/', blank=True, null=True)

class Image3(models.Model):
    image3=models.ImageField(upload_to='images/', blank=True, null=True)

class Image4(models.Model):
    image4=models.ImageField(upload_to='images/', blank=True, null=True)

class Image5(models.Model):
    image5=models.ImageField(upload_to='images/', blank=True, null=True)

class Image6(models.Model):
    image6=models.ImageField(upload_to='images/', blank=True, null=True)

class Image7(models.Model):
    image7=models.ImageField(upload_to='images/', blank=True, null=True)

class Image8(models.Model):
    image8=models.ImageField(upload_to='images/', blank=True, null=True)

class Image9(models.Model):
    image9=models.ImageField(upload_to='images/', blank=True, null=True)