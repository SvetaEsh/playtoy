from typing import Any, Dict
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
#from django.views.generic import TemplateView, DetailView
from django.views import generic
from . import models
from . import forms
from django.urls import reverse_lazy

# Create your views here.


class ProductListView(generic.ListView):
    model=models.Product
    template_name="product/list-product.html"
    form_class=forms.ProductModelForm


class ProductView(generic.DetailView):
    model=models.Product
    template_name="product/view-product.html"
    form_class=forms.ProductModelForm


class ProductDeleteView(generic.DeleteView):
    model=models.Product
    template_name="product/delete-product.html"
    success_url="/"
    def get_context_data(self, **kwargs):
        context= super().get_context_data(**kwargs)
        context["greeting"] = "Удалить товар"
        return context


class ProductCreateView(generic.CreateView):
    model=models.Product
    form_class=forms.ProductModelForm
    template_name="product/add-product.html"
    success_url=reverse_lazy("product:view-product")
    def get_context_data(self, **kwargs):
        context= super().get_context_data(**kwargs)
        context["greeting"] = "Добавь новый тип"
        return context


class ProductUpdateView(generic.UpdateView):
    model=models.Product
    form_class=forms.ProductModelForm
    template_name="product/update-product.html"
    success_url=reverse_lazy("product:view-product")
    def get_context_data(self, **kwargs):
        context= super().get_context_data(**kwargs)
        context["greeting"]= "Что хотите изменить"
        return context
 

