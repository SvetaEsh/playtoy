from django.shortcuts import render
from django.http import HttpResponse
from . import models

# Create your views here.
def home_page(request):
    type_pk = request.GET.get("type")
    print(type_pk)
    type_print = models.Type.objects.filter(pk=type_pk)
    html = "<ul>"
    models.Type.objects.
    for tp in type_print:
        html += f"<li> {tp.pk} Товар {tp.name}</li>"
    html += "</ul>"

    return HttpResponse(html)

def prodimport(request):
    list_data = []
    with open('import/data.txt', '+r', encoding="utf-8") as file_import:
        while True:
            # считываем строку
            line = file_import.readline()
            # прерываем цикл, если строка пустая
            if not line:
                break
            prfadd = models.Product(name)
            list_data.append(line.strip('\n'))
                             
    return HttpResponse("hello")
