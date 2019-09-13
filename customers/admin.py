from django.contrib import admin
from .models import Employee, Service, Customer, Status, Speed, Period, Subscription


# Register your models here.

admin.site.register(Employee)
admin.site.register(Customer)
admin.site.register(Service)
admin.site.register(Speed)
admin.site.register(Status)
admin.site.register(Period)


class SubscriptionAdmin(admin.ModelAdmin):
    list_display = ('customer', 'status', 'service')
    search_fields = ['customer__first_name', 'customer__last_name']
    list_filter = ('status', 'service')
    list_editable = ['status']


admin.site.register(Subscription, SubscriptionAdmin)
