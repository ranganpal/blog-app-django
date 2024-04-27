from django.db import models

# Create your models here.

class User(models.Model):
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    active = models.BooleanField()
    

class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField(max_length=100)
    image = models.ImageField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
