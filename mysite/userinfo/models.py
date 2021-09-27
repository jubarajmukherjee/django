from django.db import models

# Create your models here.
'''
class info (models.Model):
	username = models.CharField(max_length = 150)
	email = models.EmailField(max_length = 150)
	password = models.CharField(max_length = 15)
	cpassword = models.CharField(max_length = 15)
	address = models.CharField(max_length = 350)
'''

from django.db import models
 
class MyModel(models.Model):
    uname = models.CharField(max_length=200)
    email = models.EmailField()
    password = models.CharField(max_length=20)
    cpassword = models.CharField(max_length=20)
    address = models.TextField(max_length=999)


