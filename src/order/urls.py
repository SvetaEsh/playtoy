from django.urls import path
from . import views

app_name='order'
urlpatterns = [
    path('cart/', views.CartDetailView.as_view(), name="view-cart"),
    path('cart-edit/', views.CartAddDeleteItemView.as_view(), name="cart-edit"),
    path('create-order/', views.CreateOrder.as_view(), name="create-order"),
    path('complete-order/', views.OrderSuccess.as_view(), name="complete-order")
    
]