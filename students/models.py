from django.db import models

# Create your models here.
class Student(models.Model):
    full_name = models.CharField(max_length=100);
    email = models.EmailField();
    address = models.TextField(blank=True, default="Not Provided")

    phone_number = models.CharField(
        max_length=15,
        blank=True,
        default=""
    )

    date_of_birth = models.DateField(
        null=True,
        blank=True
    )
    age = models.IntegerField();
    created_at = models.DateTimeField(auto_now_add=True);

    def __str__(self):
        return self.full_name;

# create book class
class Book(models.Model):
    title = models.CharField(max_length=100);
    author = models.CharField(max_length=100);
    isbn = models.CharField(max_length=100);
    price = models.DecimalField(max_digits=10, decimal_places=2);
    published_date = models.DateField(blank=True, null=True);
    description = models.TextField(blank=True, null=True);
    is_available = models.BooleanField(default=True);
    created_at = models.DateTimeField(auto_now_add=True);

    def __str__(self):
        return self.title;