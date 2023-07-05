from django import template
from product.models import Product
from django.db.models import Q

register = template.Library()

@register.inclusion_tag('main/stockproduct-list.html', takes_context=True)
def show_top_stockproduct(context, count=10):
    stockproduct_items = Product.objects.filter(~Q(discount=0)).order_by('-discount')[:count]
    return {
        "stockproduct_items": stockproduct_items,
    }
