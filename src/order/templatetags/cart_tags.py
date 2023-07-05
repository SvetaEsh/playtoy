from django import template
from order.models import Cart

register = template.Library()

@register.simple_tag(takes_context=True)
def total_quantity(context):
    request = context['request']
    print('request ',request)
    cart_pk = request.session.get('cart_pkid')
    print('cart_pk ',cart_pk)
    if cart_pk:
        cart = Cart.objects.get(pk=cart_pk)
        print('cart ', cart)
        print(cart.total_quantity)
        return cart.total_quantity
    else:
        print("cart is none!!!")
        return ""


