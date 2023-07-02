from django.urls import path
from . import views

urlpatterns = [
    path('', views.HomePage.as_view(), name='main'),
    path('delivery', views.Delivery.as_view(), name='delivery'),
    path('contact', views.Contact.as_view(), name='contact')
    ]