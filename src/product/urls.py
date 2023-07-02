from django.urls import path
from . import views

app_name='product'
urlpatterns = [
    path('products/', views.ProductListView.as_view(), name="list-products"),
    path('product/<int:pk>', views.ProductView.as_view(), name="view-product"),
    path('product-delete/<int:pk>', views.ProductDeleteView.as_view(), name="delete-product"),
    path('product-add/', views.ProductCreateView.as_view(), name="create-product"),
    path('product-update/<int:pk>', views.ProductUpdateView.as_view(), name="update-product"),
    path('card-product/<int:pk>', views.CardProductView.as_view(), name="card-product"),    
    path('list-card-product', views.CardProductListView.as_view(), name="list-card-product"),
    path('list-card-product-type/<int:type_pk>', views.ProductFilterTypeView.as_view(), name="list-card-product-type"),
    ]