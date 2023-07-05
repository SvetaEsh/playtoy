from django import template
from product.models import Product
from order.models import GoodInCart, Order
from django.db.models import Q, Sum
from itertools import chain

register = template.Library()

@register.inclusion_tag('main/popularproduct-list.html', takes_context=True)
def show_top_popularproduct(context, count=6):
    complited_orders = Order.objects.filter(status = 4).values_list("cart_id")
    print("complited_orders: ", complited_orders)
    bought_goods = GoodInCart.objects.filter(cart_id__in=complited_orders).values('good_id').annotate(cnt=Sum('quantity')).order_by('-cnt').values_list('good_id')[:count]
    print("bought_goods: ", bought_goods)  

    bought_products = Product.objects.filter(pk__in=bought_goods)
    print("bought_products: ",bought_products)

    return {
        "popularproduct_items": bought_products,
    }