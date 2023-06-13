from typing import Any, Dict
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
#from django.views.generic import TemplateView, DetailView
from django.views import generic
from . import models
from . import forms
from django.urls import reverse_lazy

# Create your views here.


class TypeListView(generic.ListView):
    model=models.Type
    template_name="category/list-type.html"
    fields=["category", "name", "description", "picture"]


class TypeView(generic.DetailView):
    model=models.Type
    template_name="category/view-type.html"
    fields=["category", "name", "description", "picture"]


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
    success_url=reverse_lazy("category:success-page")
    def get_context_data(self, **kwargs):
        context= super().get_context_data(**kwargs)
        context["greeting"] = "Добавь новый тип"
        return context


def success_page(request):
    return render(request, template_name="category/add-succesfully.html", context={"message": f"Создан!"})


class TypeUpdateView(generic.UpdateView):
    model=models.Type
    fields=["category", "name", "description", "picture"]
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
    success_url=reverse_lazy("category:success-page")
    def get_context_data(self, **kwargs):
        context= super().get_context_data(**kwargs)
        context["greeting"] = "Добавить новую категорию"
        return context
    def get_success_url(self) -> str:
        self.object.picture_resizer
        return super().get_success_url()  

class CategoryUpdateView(generic.UpdateView):
    model=models.Category
    form_class=forms.CategoryModelForm
    template_name="category/update-category.html"
    def get_context_data(self, **kwargs):
        context= super().get_context_data(**kwargs)
        context["greeting"]= "Что хотите изменить"
        return context


       
       