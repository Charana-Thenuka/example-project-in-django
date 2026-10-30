from django.contrib import admin
from .models import Student
from .models import Book

# Register your models here.
admin.site.register(Student); # This tells Django to display your Student model in the admin interface.
admin.site.register(Book);

