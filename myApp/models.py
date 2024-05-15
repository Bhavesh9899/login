from django.db import models

class Register(models.Model):
    username = models.TextField() 
    email = models.TextField()
    password = models.TextField()
    disc = models.TextField(default='cool')