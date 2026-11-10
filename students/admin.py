from django.contrib import admin
from .models import Student
from .models import Book
from .models import Employee
from .models import Vehical

# Register your models here.
admin.site.register(Student); # This tells Django to display your Student model in the admin interface.
admin.site.register(Book);
admin.site.register(Employee);
admin.site.register(Vehical);

