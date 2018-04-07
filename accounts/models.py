from django.db import models
from django.contrib import auth
from django import forms

# Create your models here.


class User(auth.models.User,auth.models.PermissionsMixin):
    def __str__(self):
        return self.username


class ContactUs(models.Model):
    sender = models.EmailField()
    subject = models.CharField(max_length=20)
    message = models.CharField(max_length=150)

    def __str__(self):
        return self.sender
