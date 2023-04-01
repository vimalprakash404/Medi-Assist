from django.contrib import admin
from .models import Lab,Tech,Users,Address
# Register your models here.
admin.site.register(Lab)
admin.site.register(Tech)
admin.site.register(Users)
admin.site.register(Address)