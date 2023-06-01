from typing import Any, Dict
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
#from django.views.generic import TemplateView, DetailView
from django.views import generic
from . import models
from . import forms


# Create your views here.


class TypeListView(generic.ListView):
    model=models.Type
    template_name="category/list-type.html"
    fields=["category", "name", "description"]


class TypeView(generic.DetailView):
    model=models.Type
    template_name="category/view-type.html"
    fields=["category", "name", "description"]


class TypeDeleteView(generic.DeleteView):
    model=models.Type
    template_name="category/delete-type.html"
    success_url="/"
    def get_context_data(self, **kwargs):
        context= super().get_context_data(**kwargs)
        context["greeting"] = "Удалить тип"
        return context


class TypeCreateView(generic.CreateView):
    model=models.Type
    form_class=forms.TypeModelForm
    template_name="category/add-type.html"
    success_url="/added"
    def get_context_data(self, **kwargs):
        context= super().get_context_data(**kwargs)
        context["greeting"] = "Добавь новый тип"
        return context


def success_page(request):
    return render(request, template_name="category/add-succesfully.html", context={"message": f"Создан!"})


class TypeUpdateView(generic.UpdateView):
    model=models.Type
    fields=["category", "name", "description"]
    template_name="category/update-type.html"
    def get_context_data(self, **kwargs):
        context= super().get_context_data(**kwargs)
        context["greeting"]= "Что хотите изменить"
        return context
    

class CategoryListViews(generic.ListView):
    model = models.Category
    form_class = forms.CategoryModelForm
    template_name = "category/list_category.html"

class CategoryViews(generic.DetailView):
    model = models.Category
    form_class = forms.CategoryModelForm
    template_name = "category/view-category.html"
    
    
class CategoryDeleteView(generic.DeleteView):
    model=models.Category
    template_name="category/delete-category.html"
    success_url="/"
    
    
class CategoryCreateView(generic.CreateView):
    model=models.Category
    form_class=forms.CategoryModelForm
    template_name="category/add-category.html"
    success_url="/added"
    def get_context_data(self, **kwargs):
        context= super().get_context_data(**kwargs)
        context["greeting"] = "Добавить новую категорию"
        return context  

class CategoryUpdateView(generic.UpdateView):
    model=models.Category
    form_class=forms.CategoryModelForm
    template_name="category/update-category.html"
    def get_context_data(self, **kwargs):
        context= super().get_context_data(**kwargs)
        context["greeting"]= "Что хотите изменить"
        return context


       
       