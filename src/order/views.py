from django.shortcuts import render, get_object_or_404
from django.views.generic import DetailView
from . import models
from product.models import Product

# Create your views here.
class CartDetailView(DetailView):
    template_name = "order/cart.html"
    model=models.Cart
    
    def get_object(self, *args, **kwargs):
        cart_pk=self.request.session.get("cart_id")
        customers=self.request.user
        if customers.is_anonymous:
            customers=None
        cart, created = models.Cart.objects.get_or_create(
            pk=cart_pk,
            defaults={
                "customers": customers
            }
        )
        good_id=self.request.GET.get("good_id")
        quantity=self.request.GET.get("quantity")
        if good_id and quantity:
            quantity=int(quantity)
            good=Product.objects.get(pk=int(good_id))
            price=good.price
            
            good_in_cart, good_in_cart_created =models.GoodInCart.objects.get_or_create(
                cart=cart,
                good=good,
                defaults={
                    "quantity": quantity,
                    "price": price*quantity
                }
            )
            if not good_in_cart_created:
                good_in_cart.quantity = good_in_cart.quantity + quantity
                good_in_cart.price = good_in_cart.price + price*quantity
                good_in_cart.save()

            if created:
                self.request.session['card_id']=cart.pk

        return cart
    
class CartAddDeleteItemView(DetailView):
    template_name = "order/cart.html"
    model=models.Cart
    
    def get_object(self, *args, **kwargs):
        cart_pk=self.request.session.get("cart_id")
        customers=self.request.user
        if customers.is_anonymous:
            customers=None
        cart, created = models.Cart.objects.get_or_create(
            pk=cart_pk,
            defaults={
                "customers": customers
            }
        )
        good_id=self.request.GET.get("good")
        action=self.request.GET.get("action")
        if good_id and action and action in ["add", "delete"]:
            
            good=Product.objects.get(pk=int(good_id))
            price=good.price
            
            good_in_cart = get_object_or_404(
                models.GoodInCart,
                cart=cart,
                good=good,                
            )
            if action == "add":
                term=1
            else:
                term=-1
            good_in_cart.quantity=good_in_cart.quantity + term
            good_in_cart.price=good_in_cart.quantity*price
            good_in_cart.save()
        return cart
