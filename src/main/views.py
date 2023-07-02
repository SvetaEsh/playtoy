from django.shortcuts import render
from django.views import generic
from . import models


# Create your views here.
class HomePage(generic.TemplateView):
    template_name="main/home-page.html"


class Delivery(generic.TemplateView):
    template_name="main/shipping-and-payment.html"

class Contact(generic.TemplateView):
    template_name="main/contact.html"    