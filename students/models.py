from django.db import models


class Student(models.Model):

    register_number = models.CharField(
        max_length=20,
        unique=True
    )

    full_name = models.CharField(max_length=100)

    email = models.EmailField(unique=True)

    phone = models.CharField(max_length=15)

    department = models.CharField(max_length=100)

    course = models.CharField(max_length=100)

    date_of_birth = models.DateField()

    address = models.TextField(blank=True)

    created_at = models.DateTimeField(auto_now_add=True)

    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.register_number} - {self.full_name}"