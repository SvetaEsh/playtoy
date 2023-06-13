from typing import Any, Dict
from django.forms.models import BaseModelForm
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
#from django.views.generic import TemplateView, DetailView
from django.views import generic
from . import models
from . import forms
from django.urls import reverse_lazy

# Create your views here.
from PIL import Image
from pathlib import Path
def picture_resizer(image):
        print("picture_resizer")
        extention = image.file.name.split('.')[-1]
        BASE_DIR = Path(image.file.name).resolve().parent
        file_name = Path(image.file.name).resolve().name.split('.')
        for m_basewidth in [150,40]:
            im=Image.open(image.file.name)
            wpercent = (m_basewidth/float(im.size[0]))
            hsize = int((float(im.size[1])*float(wpercent)))
            im.thumbnail((m_basewidth,hsize), Image.Resampling.LANCZOS)
            im.save(str(BASE_DIR / ".".join(file_name[:-1])) + f'_{m_basewidth}_.' + extention)

class ProductListView(generic.ListView):
    model=models.Product
    template_name="product/list-product.html"
    form_class=forms.ProductModelForm
    def get_success_url(self) -> str:
        picture_resizer(self.object.picture) #_resizer        
        return super().get_success_url()

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
    def get_context_data(self, **kwargs):
        context= super().get_context_data(**kwargs)
        context["greeting"] = "Добавь новый тип"
        return context
    def get_success_url(self) -> str:
        picture_resizer(self.object.picture) #_resizer
        return super().get_success_url()

class ProductUpdateView(generic.UpdateView):
    model=models.Product
    form_class=forms.ProductModelForm
    template_name="product/update-product.html"
    def get_context_data(self, **kwargs):
        context= super().get_context_data(**kwargs)
        context["greeting"]= "Что хотите изменить"
        return context
    def form_valid(self, form):
        if form.has_changed():
            if 'picture' in form.changed_data:
                self.object.picture_resizer
            return super().form_valid(form)
