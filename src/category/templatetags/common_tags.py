from django import template
from category.models import Category
register = template.Library()


@register.inclusion_tag('category/menu-category.html', takes_context=True)
def show_top_menu(context):
    menu_items = Category.objects.all()
    return {
        "menu_items": menu_items,
    }