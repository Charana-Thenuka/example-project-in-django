from django.contrib import admin
from .models import Student
from .models import Book
from .models import Employee
from .models import Vehical

# Register your models here.
# admin.site.register(Student); # This tells Django to display your Student model in the admin interface.
# admin.site.register(Book);

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):

    list_display = (
        'id',
        'full_name',
        'email',
        'phone_number',
        'age',
        'created_at',
    )

    search_fields = (
        'full_name',
        'email',
        'phone_number',
    )

    list_filter = (
        'age',
        'created_at',
    )

    ordering = ('-created_at',)

    list_per_page = 10

    readonly_fields = ('created_at',)

@admin.register(Book)
class AdminBook(admin.ModelAdmin):

    list_display = (
        'id',
        'title',
        'author',
        'price',
        'description',
        'is_available',
        'created_at'
    )

    search_fields = (
        'title',
        'author',
        'description'
    )

    list_filter = (
        'author',
        'is_available',
    )

    ordering = ('-created_at',)
    
    list_per_page = 10
    
    readonly_fields = ('created_at',)


