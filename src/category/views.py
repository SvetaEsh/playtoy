from typing import Any, Dict
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
#from django.views.generic import TemplateView, DetailView
from django.views import generic
from . import models
from . import forms
from django.urls import reverse_lazy
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.


class TypeListView(generic.ListView):
    model=models.Type
    template_name="category/list-type.html"
    fields=["category", "name", "description", "picture"]


class TypeView(generic.DetailView):
    model=models.Type
    template_name="category/view-type.html"
    fields=["category", "name", "description", "picture"]


class TypeDeleteView(PermissionRequiredMixin, generic.DeleteView):
    login_url=reverse_lazy('staff:login')
    model=models.Type
    template_name="category/delete-type.html"
    success_url="/"
    permission_required=["category.delete_type"]
    def get_context_data(self, **kwargs):
        context= super().get_context_data(**kwargs)
        context["greeting"] = "Удалить тип"
        return context


class TypeCreateView(PermissionRequiredMixin, generic.CreateView):
    login_url=reverse_lazy('staff:login')
    model=models.Type
    form_class=forms.TypeModelForm
    template_name="category/add-type.html"
    success_url=reverse_lazy("category:success-page")
    permission_required=["category.add_type"]
    def get_context_data(self, **kwargs):
        context= super().get_context_data(**kwargs)
        context["greeting"] = "Добавь новый тип"
        return context
    def get_success_url(self) -> str:
        self.object.picture_resizer
        return super().get_success_url() 


def success_page(request):
    return render(request, template_name="category/add-succesfully.html", context={"message": f"Создан!"})


class TypeUpdateView(PermissionRequiredMixin, generic.UpdateView):
    login_url=reverse_lazy('staff:login')
    model=models.Type
    fields=["category", "name", "description", "picture"]
    template_name="category/update-type.html"
    permission_required=["category.update_type"]
    def get_context_data(self, **kwargs):
        context= super().get_context_data(**kwargs)
        context["greeting"]= "Что хотите изменить"
        return context    
    def get_success_url(self) -> str:        
        self.object.picture_resizer() #_resizer
        return super().get_success_url()

class CategoryListViews(generic.ListView):
    model = models.Category
    form_class = forms.CategoryModelForm
    template_name = "category/list_category.html"

class CategoryViews(generic.DetailView):
    model = models.Category
    form_class = forms.CategoryModelForm
    template_name = "category/view-category.html"
    
    
class CategoryDeleteView(PermissionRequiredMixin, generic.DeleteView):
    login_url=reverse_lazy('staff:login')
    model=models.Category
    template_name="category/delete-category.html"
    success_url="/"
    permission_required=["category.delete_category"]
    
class CategoryCreateView(PermissionRequiredMixin, generic.CreateView):
    login_url=reverse_lazy('staff:login')
    model=models.Category
    form_class=forms.CategoryModelForm
    template_name="category/add-category.html"
    success_url=reverse_lazy("category:success-page")
    
    permission_required=["category.add_category"]

    def get_context_data(self, **kwargs):
        context= super().get_context_data(**kwargs)
        context["greeting"] = "Добавить новую категорию"
        return context
    
 
class CategoryUpdateView(PermissionRequiredMixin, generic.UpdateView):
    login_url=reverse_lazy('staff:login')
    model=models.Category
    fields=["name", "description", "picture"]
    template_name="category/update-category.html"
    permission_required=["category.update_category"]
    def get_context_data(self, **kwargs):
        context= super().get_context_data(**kwargs)
        context["greeting"]= "Что хотите изменить"
        return context
    



       
       