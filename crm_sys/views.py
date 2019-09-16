from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import CustomerForm
from .models import Customer

# Create your views here.


def login(request):
    if request.POST:
        return redirect("customer/")
    else:
        return render(request, 'login.html', {})


def create_customer(request):
    if request.method == "POST":
        form = CustomerForm(request.POST or None)
        if form.is_valid():
            form.save()
        return redirect('/customer/')
    else :
        create_customer_form = CustomerForm()
        return render(request, 'create_customer.html', {'form': create_customer_form})


def customer_portal(request):
    customers = Customer.objects.all()
    context = {
        'customers': customers
    }
    return render(request, 'customer.html', context)


def customer_profile(request, customer_ssd=0):
    if customer_ssd == 0:
        return redirect('/customer/')
    else:
        if request.method == "POST":
            print("passed 1 ")
            form = CustomerForm(request.POST or None)
            print(form.errors.as_data())
            if form.is_valid():
                print("passed 2 ")
                customer = Customer.objects.get(ssd=customer_ssd)
                form.save()
                print(form)
                context = {
                    'customer': customer
                }
                context['form'] = form
                return render(request, 'profile.html', context)

        customer = Customer.objects.get(ssd=customer_ssd)
        context = {
            'customer': customer
        }
        form = CustomerForm(instance=customer)
        context['form'] = form
    return render(request, 'profile.html', context)
