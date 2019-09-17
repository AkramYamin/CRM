from django.shortcuts import render, redirect
from django.http import HttpResponse
from .forms import CustomerForm ,SubscriptionForm
from .models import Customer, Subscription

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
            print("user_created")
            customer = form.save(commit=False)
            print("pass1")
            customer.save()
            subscriptions = form.cleaned_data['subscriptions']
            print(subscriptions)
            for it in subscriptions:
                print(it.id)
                sub = Subscription(service=it, customer=customer)
                sub.save()
                print("pass2")
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
            form = CustomerForm(request.POST or None, instance=Customer.objects.get(ssd=customer_ssd))
            if form.is_valid():
                customer = form.save(commit=False)
                customer.save()
                Subscription.objects.filter(customer=Customer.objects.get(ssd=customer_ssd)).delete()
                subscriptions = form.cleaned_data['subscriptions']
                print(subscriptions)
                for it in subscriptions:
                    print(it.id)
                    sub = Subscription(service=it, customer=customer)
                    sub.save()
                print("updated")
                context = {'customer': customer,
                           'form': form
                           }
                return render(request, 'profile.html', context)

        customer = Customer.objects.get(ssd=customer_ssd)
        context = {
            'customer': customer,
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
        customers = Customer.objects.filter(first_name__icontains=content, )
        customers |= Customer.objects.filter(last_name__icontains=content, )
    print(customers)
    context = {
        'customers': customers
    }
    return render(request, 'customer.html', context)
