from django import forms
from .models import Customer, Subscription


class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        fields = "__all__"


class SubscriptionForm(forms.ModelForm):
    class Meta:
        model = Subscription
        fields = "__all__"
