from email.policy import default
from re import L
from unicodedata import name
from django.db import models
from django.forms import IntegerField
from account.models import Lab
from django.contrib.auth.models import User
# Create your models here.







class Test(models.Model):
    lab=models.ForeignKey(Lab, on_delete=models.CASCADE)
    name=models.CharField( max_length=50)
    cost=models.FloatField()
    duration=models.TimeField( auto_now=False, auto_now_add=False)
    def __str__(self) :
        return self.name

class booking(models.Model):
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    test=models.ForeignKey(Test, on_delete=models.CASCADE)
    date=models.DateField(auto_now=False, auto_now_add=False)
    token=models.IntegerField()
    status=models.CharField(max_length=50,default="pending")

class Report(models.Model):
    user=models.ForeignKey(User, on_delete=models.CASCADE)
    test=models.OneToOneField(booking, on_delete=models.CASCADE)
    givendate=models.DateField()
    compltedate=models.DateField(auto_now=False, auto_now_add=False)
    report=models.CharField(max_length=50)
    def __str__(self) :
        return self.report

class Token(models.Model):
    lab=models.ForeignKey(Lab, on_delete=models.CASCADE)
    date=models.DateField( auto_now=False, auto_now_add=False)
    current_token=models.IntegerField()