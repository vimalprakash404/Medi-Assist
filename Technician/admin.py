from django.contrib import admin
from .models import Test, booking
# Register your models here.

admin.site.register(booking)
admin.site.register(Test)