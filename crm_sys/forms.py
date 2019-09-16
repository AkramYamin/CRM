from django import forms
from .models import Customer, Service


class CustomerForm(forms.ModelForm):
    class Meta:
        model = Customer
        exclude = ('subscriptions',)


class SubscriptionForm (forms.ModelForm):
    class Meta:
        model = Customer
        fields = ("subscriptions", )

    def __init__ (self, *args, **kwargs):
        super(SubscriptionForm, self).__init__(*args, **kwargs)
        self.fields["subscriptions"].widget = forms.widgets.CheckboxSelectMultiple()
        self.fields["subscriptions"].help_text = ""
        self.fields["subscriptions"].queryset = Customer.objects.all()
