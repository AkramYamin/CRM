from django.urls import include, path
from . import views

urlpatterns = [
    path('', views.login, name='login'),
    path('customer/', views.customer_portal, name='customer_portal'),
    path('customer/cprofile/', views.customer_profile, name='customer_profile'),
]