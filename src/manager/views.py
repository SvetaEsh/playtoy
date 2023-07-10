from django.shortcuts import render
from django.contrib.auth.decorators import permission_required

# Create your views here.

def manager_page(request):
    return render(request, template_name="manager/manager.html", context={"message": f"Привет, менеджер!"})
