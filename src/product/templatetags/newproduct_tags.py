from django import template
from product.models import Product
register = template.Library()

@register.inclusion_tag('product/newproduct-list.html', takes_context=True)
def show_top_newproduct(context, count=12):
    newproduct_items = Product.objects.order_by('-created')[:count]
    return {
        "newproduct_items": newproduct_items,
    }