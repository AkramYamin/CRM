from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import CustomerForm, SubscriptionForm
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
        subscriptions_form = SubscriptionForm(request.POST or None)
        context = {
            'customer': customer,
            'subscriptions_form': subscriptions_form
        }
        form = CustomerForm(instance=customer)
        context['form'] = form
    return render(request, 'profile.html', context)


def search(request):
    content = request.GET.__getitem__('search')
    url = '/customer/search/' + content + '/'
    return redirect(url)


def search_customer(request, content):
    try:
        ssd = int(content)
        customers = Customer.objects.filter(ssd__in=[content],
                                            )
    except ValueError:
        customers = Customer.objects.filter(first_name__icontains=content,
                                            )
        customers |= Customer.objects.filter(last_name__icontains=content,
                                            )
    print(customers)
    context = {
        'customers': customers
    }
    return render(request, 'customer.html', context)
