from django.contrib import admin
from .models import Employee, Service, Customer, Status, Speed, Period, Subscription


# Register your models here.

"""
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'email', 'phone', 'ssd', 'is_active')
    list_editable = ['phone', 'email', 'is_active']
    search_fields = ['first_name', 'last_name', 'email', 'ssd']
    list_filter = ['is_active']


admin.site.register(Employee, EmployeeAdmin)
"""


class RoleInline(admin.TabularInline):
    model = Subscription
    extra = 1


class CustomerAdmin(admin.ModelAdmin):
    inlines = (RoleInline,)
    list_display = ('first_name', 'last_name', 'ssd', '_subscriptions', 'access_speed', 'phone', 'is_active')
    search_fields = ('first_name', 'second_name', 'ssd', 'access_speed__speed')
    list_editable = ['phone', 'is_active']
    list_filter = ['access_speed', 'is_active']


admin.site.register(Customer, CustomerAdmin)


class ServiceAdmin(admin.ModelAdmin):
    list_display = ('name', 'description', 'price', 'period', 'speed', 'is_active')
    search_fields = ('name', 'description')
    list_editable = ('is_active', )
    list_filter = ['speed', 'period', 'is_active']


admin.site.register(Service, ServiceAdmin)


class SpeedAdmin(admin.ModelAdmin):
    search_fields = ['speed']


admin.site.register(Speed, SpeedAdmin)


class StatusAdmin(admin.ModelAdmin):
    list_display = ('name', 'description')
    search_fields = ('name', 'description')


admin.site.register(Status, StatusAdmin)


class PeriodAdmin(admin.ModelAdmin):
    list_display = ('period', 'description')
    search_fields = ('period', 'description')


admin.site.register(Period, PeriodAdmin)


class SubscriptionAdmin(admin.ModelAdmin):
    list_display = ('customer', 'status', 'service')
    search_fields = ['customer__first_name', 'customer__last_name']
    list_filter = ('status', 'service')
    list_editable = ['status']


admin.site.register(Subscription, SubscriptionAdmin)
