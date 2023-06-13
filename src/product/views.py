from django.views import generic
from . import models
from . import forms
from django.conf import settings
import os
from pathlib import Path
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

class ProductView(generic.DetailView):
    model=models.Product
    template_name="product/view-product.html"
    form_class=forms.ProductModelForm

class CardProductListView(generic.ListView):
    model=models.Product
    template_name="product/list-card-product.html"

class CardProductView(generic.DetailView):
    model=models.Product
    template_name="product/card-product.html"
    #form_class=forms.ProductModelForm

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
        self.object.picture_resizer() #_resizer
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
            if "picture" in form.changed_data:
                old_img = os.path.join(settings.MEDIA_ROOT+str(form.initial["picture"]))
                picture_deletizer(old_img)
        return super().form_valid(form)
    def get_success_url(self) -> str:        
        self.object.picture_resizer() #_resizer
        return super().get_success_url()

