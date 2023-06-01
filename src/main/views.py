from django.shortcuts import render
from django.views import generic
from . import models


# Create your views here.
class HomePage(generic.TemplateView):
    template_name="main/home-page.html"