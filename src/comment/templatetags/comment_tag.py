from django import template
from comment import models
from django.contrib.contenttypes.models import ContentType

register = template.Library()


@register.inclusion_tag('comment/comments.html', takes_context=True)
def comments_tag(context, obj):
    content_type = ContentType.objects.get_for_model(obj)
    comments=models.Comment.objects.filter(
        content_type = content_type,
        object_id=obj.pk)
    return {
        "comments": comments,
        "object_id": obj.pk,
        "content_type": content_type
    }