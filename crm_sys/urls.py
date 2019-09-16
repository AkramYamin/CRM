from django.urls import include, path
from . import views

urlpatterns = [
    path('', views.customer_portal, name='customer_portal'),
    path('profile/<int:customer_ssd>/', views.customer_profile, name='customer_profile'),
    path('create_customer/', views.create_customer, name='create_customer'),
]
