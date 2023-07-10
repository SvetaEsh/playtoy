from django.views import generic
from . import models
from . import forms
from django.conf import settings
import os
from pathlib import Path
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.urls import reverse_lazy
# Create your views here.

def picture_deletizer(path):
        print("class picture_deletizer")
        extention = path.split('.')[-1]
        BASE_DIR = Path(path).resolve().parent
        file_name = Path(path).resolve().name.split('.')
        os.remove(path)
        for m_basewidth in [150,40]:
            os.remove(str(BASE_DIR/".".join(file_name[:-1])) + f'_{m_basewidth}_.' + extention)

class ProductListView(generic.ListView):
    model=models.Product
    template_name="product/list-product.html"
    form_class=forms.ProductModelForm

"""
class NewProductListView(generic.ListView):
    model=models.Product
    template_name="product/list-new-product.html"
    form_class=forms.ProductModelForm    
    def get_queryset(self):
        return super().get_queryset().annotate().order_by('-created')[:10]    
"""
class ProductView(generic.DetailView):
    model=models.Product
    template_name="product/view-product.html"
    form_class=forms.ProductModelForm

class ProductFilterTypeView(generic.ListView):
    model=models.Product
    template_name="product/list-card-product-type.html"
    form_class=forms.ProductModelForm    

class CardProductListView(generic.ListView):
    model=models.Product
    template_name="product/list-card-product.html"

class CardProductView(generic.DetailView):
    model=models.Product
    template_name="product/card-product.html"
    #form_class=forms.ProductModelForm

class ProductDeleteView(PermissionRequiredMixin, generic.DeleteView):
    login_url=reverse_lazy('staff:login')
    model=models.Product
    template_name="product/delete-product.html"
    success_url="/"
    permission_required=["product.add_product"]
    def get_context_data(self, **kwargs):
        context= super().get_context_data(**kwargs)
        context["greeting"] = "Удалить товар"
        return context

class ProductCreateView(PermissionRequiredMixin, generic.CreateView):
    login_url=reverse_lazy('staff:login')
    model=models.Product
    form_class=forms.ProductModelForm
    template_name="product/add-product.html"
    permission_required=["product.add_product"]
    def get_context_data(self, **kwargs):
        context= super().get_context_data(**kwargs)
        context["greeting"] = "Добавь новый товар"
        return context
    def get_success_url(self) -> str:
        self.object.picture_resizer() #_resizer
        return super().get_success_url()

class ProductUpdateView(PermissionRequiredMixin, generic.UpdateView):
    login_url=reverse_lazy('staff:login')
    model=models.Product
    form_class=forms.ProductModelForm
    template_name="product/update-product.html"
    permission_required=["product.update_product"]
    def get_context_data(self, **kwargs):
        context= super().get_context_data(**kwargs)
        context["greeting"]= "Что хотите изменить"
        return context
    def form_valid(self, form):
        if form.has_changed():
            if "picture" in form.changed_data:
                old_img = os.path.join(settings.MEDIA_ROOT+str(form.initial["picture"]))
                picture_deletizer(old_img)
        return super().form_valid(form)
    def get_success_url(self) -> str:        
        self.object.picture_resizer() #_resizer
        return super().get_success_url()

