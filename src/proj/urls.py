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
from django.urls import path, include
from category import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('main.urls')),
    path('type-cbv/', views.TypeListView.as_view()),
    path('type-cbv/<int:pk>', views.TypeView.as_view()),
    path('type-delete-cbv/<int:pk>', views.TypeDeleteView.as_view()),
    path('type-add-cbv/', views.TypeCreateView.as_view()),
    path('added/', views.success_page),
    path('type-update-cbv/<int:pk>', views.TypeUpdateView.as_view()),
    path('category-cbv/', views.CategoryListViews.as_view()),
    path('category-cbv/<int:pk>', views.CategoryViews.as_view()),
    path('category-delete-cbv/<int:pk>', views.CategoryDeleteView.as_view()), 
    path('category-add-cbv/', views.CategoryCreateView.as_view()),
    path('category-update-cbv/<int:pk>', views.CategoryUpdateView.as_view())
]
#<img src="{{object.book_image}}" alt=" ">rk.