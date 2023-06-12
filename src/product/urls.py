from django.urls import path
from . import views

app_name='product'
urlpatterns = [
    path('products/', views.ProductListView.as_view(), name="list-products"),
    path('product/<int:pk>', views.ProductView.as_view(), name="view-product"),
    path('product-delete/<int:pk>', views.ProductDeleteView.as_view(), name="delete-product"),
    path('product-add/', views.ProductCreateView.as_view(), name="create-product"),
    path('product-update/<int:pk>', views.ProductUpdateView.as_view(), name="update-product"),
    ]