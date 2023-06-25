from django.shortcuts import render, get_object_or_404
from django.views.generic import DetailView, CreateView, FormView
from . import models, forms
from order.models import Status
from product.models import Product
from django.conf import settings

# Create your views here.
class CartDetailView(DetailView):
    template_name = "order/cart.html"
    model=models.Cart
    
    def get_object(self, *args, **kwargs):
        cart_pk=self.request.session.get('cart_pkid')
        print("start ", cart_pk)
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
                self.request.session['cart_pkid']=cart.pk
            print("start ", cart.pk)    

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
                if good_in_cart.quantity <= 1:
                    good_in_cart.delete()
                    return cart
                term=-1
            good_in_cart.quantity=good_in_cart.quantity + term
            good_in_cart.price=good_in_cart.quantity*price
            good_in_cart.save()
        return cart

class CreateOrder(FormView):
    form_class = forms.CreateOrderForm
    template_name="order/create_order.html"
    def form_valid(self, form):
        adress=form.cleaned_data.get("adress")
        print(adress)
        telefon=form.cleaned_data.get("telefon")
        print(telefon)
        print(settings.ORDER_STATUS_NEW)
        status=Status.objects.get(pk=settings.ORDER_STATUS_NEW)
        cart_pk=self.request.session.get("cart_id")
        print(cart_pk)
        cart = get_object_or_404(
                models.Cart,
                pk=int(cart_pk)                               
            )
        obj= models.Order.objects.create(
            adress=adress,
            telefon=telefon,
            status=status,
            cart=cart
        )
        return super().form_valid(form)
    