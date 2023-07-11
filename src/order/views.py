from django.shortcuts import render, get_object_or_404
from django.views.generic import DetailView, TemplateView, FormView
from django.views import generic
from django.urls import reverse_lazy
from . import models, forms
from order.models import Status, GoodInCart, Cart, Order
from product.models import Product
from django.conf import settings
from django.contrib.auth.mixins import PermissionRequiredMixin

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
        action=self.request.GET.get("action")
        if good_id and action and action in ['add', 'delete']:
            
            good=Product.objects.get(pk=int(good_id))
            price=good.price
            
            good_in_cart = get_object_or_404(
                models.GoodInCart,
                cart=cart,
                good=good
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

        print("start ", cart.pk)    
        return cart

class CreateOrder(FormView):
    form_class = forms.CreateOrderForm
    template_name="order/create_order.html"
    success_url=reverse_lazy("order:complete-order")
    def form_valid(self, form):
        adress=form.cleaned_data.get("adress")
        print(adress)
        telefon=form.cleaned_data.get("telefon")
        print(telefon)
        print(settings.ORDER_STATUS_NEW)
        status=Status.objects.get(pk=settings.ORDER_STATUS_NEW)
        cart_pk=self.request.session.get("cart_pkid")
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
        del self.request.session["cart_pkid"]
        return super().form_valid(form)
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        cart_id=self.request.session.get("cart_pkid")

        context["object"] = get_object_or_404(
            models.Cart,
            pk=int(cart_id)
        )
        return context
    

class OrderSuccess(TemplateView):               
        template_name = "order/order-complete.html"

def  history_order(request):
    data=[]
    user_id = None
    
    if request.user.is_authenticated:
        user_id = request.user
    # Получили все картs
    carts = Cart.objects.filter(customers=user_id)
    print("\ncarts : ", carts)

    # Получили все заказы связанные с картой
    orders = Order.objects.filter(cart_id__in=carts)
    print("\norders : ", orders)
    
    for order in orders:
        carts_items = order.cart.goods.all()
        # следущая строка - то же самое но через фильтр
        # carts_items = GoodInCart.objects.filter(cart=order.cart)
        data_items = []
        for carts_item in carts_items:
            data_items.append(carts_item)
        data.append((order,data_items))
        
    context = {"result": data}
    return render(request, template_name="order/history-order.html",context=context)

class OrderDeleteView(generic.DeleteView):
    
    model=models.Order
    template_name="order/delete-order.html"
    success_url=reverse_lazy("order:history-order")

def  all_order(request):
    data=[]
    user_id = None
    
    
    # Получили все картs
    carts = Cart.objects.all()
    print("\ncarts : ", carts)

    # Получили все заказы связанные с картой
    orders = Order.objects.filter(cart_id__in=carts)
    print("\norders : ", orders)
    
    for order in orders:
        carts_items = order.cart.goods.all()
        # следущая строка - то же самое но через фильтр
        # carts_items = GoodInCart.objects.filter(cart=order.cart)
        data_items = []
        for carts_item in carts_items:
            data_items.append(carts_item)
        data.append((order,data_items))
        
    context = {"result": data}
    return render(request, template_name="order/all-order.html",context=context)
      

class OrderUpdateView(PermissionRequiredMixin, generic.UpdateView):
    login_url=reverse_lazy('staff:login')
    model=models.Order
    fields=["adress", "telefon", "status"]
    template_name="order/update-order.html"
    permission_required=["category.update_order"]
    success_url=reverse_lazy("order:all-order")