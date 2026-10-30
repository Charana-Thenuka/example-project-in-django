from django.contrib import admin
from .models import Student

# Register your models here.
admin.site.register(Student); # This tells Django to display your Student model in the admin interface.

