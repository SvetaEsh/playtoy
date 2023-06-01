from django.shortcuts import render

# Create your views here.
class HomePage(generic.TemplateView):
    template_name="main/home-page.html"