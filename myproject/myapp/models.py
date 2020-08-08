from django.db import models

# Create your models here.
class Register(models.Model):
    name = models.CharField(max_length=30)
    email = models.EmailField(max_length=50)
    text = models.CharField(max_length =100)

    def __str__(self):
        return self.name

class Python(models.Model):
    session = models.CharField(max_length=30, unique=True)

    def __str__(self):
        return self.session

class Student(models.Model):
    name = models.CharField(max_length= 30, unique = False)
    session= models.ForeignKey("Python", on_delete=models.PROTECT)

    def __str__(self):
        return self.name

class Login(models.Model):
    username = models.CharField(max_length=40)
    email = models.EmailField(max_length=50)
    password = models.CharField(max_length=50)

    def __str__(self):
        return self.username

