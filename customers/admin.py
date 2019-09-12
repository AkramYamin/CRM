from django.contrib import admin
from .models import Employee, Service, Customer


# Register your models here.

admin.site.register(Employee)
admin.site.register(Customer)
admin.site.register(Service)