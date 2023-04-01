from pyexpat import model
from django import forms
from Technician.models import Test ,booking,Report

class Testforms(forms.ModelForm):
    class Meta:
        model=Test
        exclude = ['lab']

class Bookfrom(forms.ModelForm):
    class Meta:
        model=booking
        exclude = ["user",]

class Reportform(forms.ModelForm):
    class Meta:
        model=Report
        exclude = ['test','user','givendate']