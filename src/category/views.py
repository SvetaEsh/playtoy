from django.shortcuts import render
from django.http import HttpResponse
from . import models

# Create your views here.
def home_page(request):
    type_pk = request.GET.get("type")
    print(type_pk)
    type_print = models.Type.objects.filter(pk=type_pk)
    html = "<ul>"

    for tp in type_print:
        html += f"<li> {tp.pk} Товар {tp.name}</li>"
    html += "</ul>"

    return HttpResponse(html)

def prodimport(request):


    return HttpResponse("hello")
