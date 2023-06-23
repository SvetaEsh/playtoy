from django.urls import path
from . import views

app_name='order'
urlpatterns = [
    path('cart/', views.CartDetailView.as_view(), name="view-cart"),
    path('cart-items-edit/', views.CartAddDeleteItemView.as_view(), name="cart-items-edit")
    
]