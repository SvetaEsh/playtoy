"""
URL configuration for proj project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from category import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('type/', views.list_type),
    path('type/<int:pk>', views.views_type),
    path('type-delete/<int:pk>', views.delete_type),
    path('category/', views.list_category),
    path('category/<int:pk>', views.views_category),
    path('category-delete/<int:pk>', views.delete_category)
]
