from django.db import models
from phonenumber_field.modelfields import PhoneNumberField

# Create your models here.


class Speed(models.Model):
    speed = models.SmallIntegerField()

    def __str__(self):
        return str(self.speed)


class Period(models.Model):
    period = models.SmallIntegerField()
    description = models.TextField()

    def __str__(self):
        return self.description


class Status(models.Model):
    name = models.CharField(max_length=60)
    description = models.TextField()

    def __str__(self):
        return self.name


class Service(models.Model):
    name = models.CharField(max_length=250)
    description = models.TextField()
    price = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateField(auto_now=True)
    is_active = models.BooleanField(default=True)
    speed = models.ForeignKey(Speed, on_delete=models.CASCADE)
    period = models.ForeignKey(Period, on_delete=models.CASCADE)

    def __str__(self):
        return self.description


class Customer(models.Model):
    first_name = models.CharField(max_length=250)
    last_name = models.CharField(max_length=250)
    first_address = models.CharField(max_length=500)
    second_address = models.CharField(max_length=500)
    phone = PhoneNumberField(unique=True)
    ssd = models.PositiveIntegerField(unique=True)
    created_at = models.DateTimeField(auto_now_add=True)
    last_modified = models.DateTimeField(auto_now=True)
    access_speed = models.ForeignKey(Speed, on_delete=models.CASCADE)
    subscriptions = models.ManyToManyField(Service, through='Subscription')
    is_active = models.BooleanField(default=True)

    def subscriptions_(self):
        text = "\n".join([p.name for p in self.subscriptions.all()])
        if text == "":
            text = "not subscriptions"
        return text

    def __str__(self):
        return self.first_name + " " + self.last_name


class Subscription(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.PROTECT)
    service = models.ForeignKey(Service, on_delete=models.PROTECT)
    status = models.ForeignKey(Status, on_delete=models.PROTECT, default=1)
    joined_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return str(self.customer)
