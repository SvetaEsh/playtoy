from django.shortcuts import render
from category import models
from product import models
from django.db.models import Q


# Create your views here.
def search_view(request):
        
    res = []
    q = None

    if request.method == "POST":
        q = request.POST.get("q")   
        print("q: ",q)    
    
        categories=models.Category.objects.filter(
            Q(name__icontains="q[0].upper()+q[1:]") | Q(name__icontains=q) | Q(name__icontains=q.lower()) | Q(name__icontains=q[0]+q[1:].lower()))
        print(categories)
        typies=models.Type.objects.filter(Q(name__icontains=q[0].upper()+q[1:]) | Q(name__icontains=q) | Q(name__icontains=q.lower()) | Q(name__icontains=q[0]+q[1:].lower()))
        print(typies)
        products=models.Product.objects.filter(Q(name__icontains=q[0].upper()+q[1:]) | Q(name__icontains=q) | Q(name__icontains=q.lower()) | Q(name__icontains=q[0]+q[1:].lower()))
        print(products)

        for obj in categories:
            res.append((obj.name,obj.get_absolute_url()))
        for obj in typies:
            res.append((obj.name,obj.get_absolute_url()))
        for obj in products:
            res.append((obj.name,obj.get_absolute_url()))
    context = {"result": res,"q": q }
    return render(request, template_name="search/search_result.html", context=context)
    