from django.db import models


class Reach(models.Model):
    firstname=models.CharField(max_length=122)
    lastname=models.CharField(max_length=122)
    mail=models.CharField(max_length=122)
    phone=models.CharField(max_length=122)
    desc=models.TextField(max_length=122)
    # slug = models.SlugField(unique=True, null=True)
    def __str__(self):
        return self.firstname
class Customer_Signup(models.Model):
    firstname=models.CharField(max_length=122)
    lastname=models.CharField(max_length=122)
    mail=models.CharField(max_length=122)
    phone=models.CharField(max_length=122)
    password=models.CharField(max_length=50)
    address=models.CharField(max_length=122)
    
    def __str__(self):
        return self.firstname
class Tailor_Signup(models.Model):
    firstname=models.CharField(max_length=122)
    lastname=models.CharField(max_length=122)
    mail=models.CharField(max_length=122)
    phone=models.CharField(max_length=122)
    password=models.CharField(max_length=50)
    shopname=models.CharField(max_length=122)
    address=models.CharField(max_length=122)
    
    def __str__(self):
        return self.firstname