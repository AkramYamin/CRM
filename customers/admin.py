from django.contrib import admin
from .models import Employee, Service, Customer, Status, Speed, Period, Subscription


# Register your models here.

admin.site.register(Employee)
admin.site.register(Customer)
admin.site.register(Service)
admin.site.register(Speed)
admin.site.register(Status)
admin.site.register(Period)
admin.site.register(Subscription)
