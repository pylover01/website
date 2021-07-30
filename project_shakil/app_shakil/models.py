from django.db import models

# Create your models here.
class Users(models.Model):
    first_name = models.CharField(max_length=50)
    dob = models.DateTimeField('Date of Birth')
    user_email = models.CharField(max_length=100)
    password = models.CharField(max_length=200)

class Blog(models.Model):
    user = models.ForeignKey(Users, on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    body = models.CharField(max_length=2000)