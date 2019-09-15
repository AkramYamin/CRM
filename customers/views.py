from django.shortcuts import render


# Create your views here.


def login(request):
    return render(request, 'login.html', {})


def customer_portal(request):
    return render(request, 'customer.html', {})


def customer_profile(request):
    return render(request, 'cprofile.html', {})
