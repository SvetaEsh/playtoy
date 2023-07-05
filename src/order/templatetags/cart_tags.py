from django import template
from order.models import Cart

register = template.Library()

@register.simple_tag(takes_context=True)
def total_quantity(context):
    request = context['request']
    cart_pk = request.session.get('cart_pkid')
    cart = Cart.objects.get(pk=cart_pk)
    return cart.total_quantity


