from django.shortcuts import render
from django.http import HttpResponse
from . import models

# Create your views here.
def list_type(request):
    types = models.Type.objects.all()
    return render(request, template_name="category/list-type.html", context={'types': types})


def views_type(request, pk):
    type=models.Type.objects.get(pk=int(pk))
    return render(request, template_name="category/view-type.html", context={'type': type})


def delete_type(request, pk):
    models.Type.objects.get(pk=int(pk)).delete()
    return render(request, template_name="category/delete-type.html", context={'type': type})


def list_category(request):
    categories = models.Category.objects.all()
    return render(request, template_name="category/list_category.html", context={'categories': categories})


def views_category(request, pk):
    category=models.Category.objects.get(pk=int(pk))
    types=models.Type.objects.filter(category=int(pk))
    return render(request, template_name="category/view-category.html", context={'category': category, 'types': types})


def delete_category(request, pk):
    models.Category.objects.get(pk=int(pk)).delete()
    return render(request, template_name="category/delete-category.html", context={'category': category})