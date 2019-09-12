from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

# Create your models here.


class Service(models.Model):
    name = models.CharField(max_length=250)
    description = models.TextField()
    price = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateField(auto_now=True)

    def __str__(self):
        return self.name


class Employee(models.Model):
    name = models.CharField(max_length=250)
    phone = PhoneNumberField()
    username = models.CharField(max_length=15)
    password = models.CharField(max_length=500)
    first_address = models.CharField(max_length=500)
    second_address = models.CharField(max_length=500)
    email = models.EmailField()
    is_admin = models.BooleanField(default=True)
    is_active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Customer(models.Model):
    name = models.CharField(max_length=250)
    first_address = models.CharField(max_length=500)
    second_address = models.CharField(max_length=500)
    phone = PhoneNumberField()
    ssd = models.PositiveIntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    created_by = models.ForeignKey(Employee, on_delete=models.PROTECT, related_name='created_by')
    last_modified = models.DateTimeField(auto_now=True)
    modified_by = models.ForeignKey(Employee, on_delete=models.PROTECT, related_name='modified_by')
    deleted_at = models.DateTimeField(null=True)
    deleted_by = models.ForeignKey(Employee, on_delete=models.PROTECT, related_name='deleted_by')
    subscription = models.ManyToManyField(Service)

    def __str__(self):
        return self.name + "  " + self.ssd

