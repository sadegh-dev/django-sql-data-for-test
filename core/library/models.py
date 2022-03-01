from distutils.command.upload import upload
from email.policy import default
from enum import unique
from tokenize import blank_re
from turtle import update
from django.db import models


class Person(models.Model):
    name = models.CharField(max_length=200)
    birthday_year = models.PositiveIntegerField() 
    data = models.JSONField(null=True, blank= True)
    is_active = models.BooleanField(default=True)
    address = models.TextField(max_length=1000)
    dato = models.DateTimeField(null=True, blank=True)
    email = models.EmailField(max_length=254)
    identify = models.SlugField(blank=True, null=True)    
    website = models.URLField(null=True, blank=True)
    attach = models.FileField(blank=True, null=True, max_length=254, upload_to='files/')
    pic = models.ImageField(null=True, blank=True, upload_to = 'images/')

    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)



