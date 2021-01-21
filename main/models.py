from django.db import models

class ToDo(models.Model):
    text = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    is_closed = models.BooleanField(default=False)
    is_favorite = models.BooleanField(default=False)

class Book(models.Model):
    title = models.CharField(max_length=300)
    subtitle = models.CharField(max_length=300)
    description = models.TextField(max_length=1000)
    price = models.FloatField()
    genre = models.CharField(max_length=50)
    author = models.CharField(max_length=50)
    year = models.DateField()
    date = models.DateField(auto_now_add=True)
    isfavorite = models.BooleanField(default=False)
