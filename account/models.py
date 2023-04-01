from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Address(models.Model):
    Building_name=models.CharField(max_length=50)
    place=models.CharField(max_length=50)
    postoffice=models.CharField(max_length=50)
    pincode=models.IntegerField()
    district=models.CharField(max_length=50)
    state=models.CharField(max_length=50)
    def __str__(self) :
        return self.Building_name
class Tech(models.Model):
    user=models.OneToOneField(User, on_delete=models.CASCADE)
    def __str__(self) :
        return self.user.username

class Lab(models.Model):
    name=models.CharField(max_length=50)
    tech=models.OneToOneField(Tech, on_delete=models.CASCADE)
    Address=models.ForeignKey(Address, on_delete=models.CASCADE)
    def __str__(self) :
        return self.name
class Users(models.Model):
    user=models.OneToOneField(User, on_delete=models.CASCADE)
    def __str__(self) :
        return self.user.username
   