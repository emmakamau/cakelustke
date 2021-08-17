from django.db import models
from django.urls import reverse

# Create your models here.

class Cake(models.Model):
    caketype = models.CharField(max_length=20)
    description = models.CharField(max_length=200)
    viewcake = models.ImageField(blank=True,upload_to='media')
    
    def __str__(self):
        return self.caketype


class Gallery(models.Model):
    cakename = models.ForeignKey('Cake', on_delete=models.SET_NULL, null=True)
    cakeimage = models.ImageField(blank=False,upload_to='media')


class Review(models.Model):
    name = models.CharField(max_length=50, null=False, default='Anonymous')
    custreview = models.TextField(max_length=400)

    def __str__(self):
        return self.name

