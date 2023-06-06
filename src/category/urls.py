from django.urls import path
from . import views
app_name='category'
urlpatterns = [
    path('type/', views.TypeListView.as_view(), name="type"),
    path('type/<int:pk>', views.TypeView.as_view(), name="view-type"),
    path('type-delete/<int:pk>', views.TypeDeleteView.as_view(), name="delete-type"),
    path('type-add/', views.TypeCreateView.as_view(), name="create-type"),
    path('success-page/', views.success_page, name="success-page"),
    path('type-update/<int:pk>', views.TypeUpdateView.as_view(), name="update-type"),
    path('category/', views.CategoryListViews.as_view(), name="category"),
    path('category/<int:pk>', views.CategoryViews.as_view(), name="view-category"),
    path('category-delete/<int:pk>', views.CategoryDeleteView.as_view(), name="delete-category"), 
    path('category-add/', views.CategoryCreateView.as_view(), name="create-category"),
    path('category-update/<int:pk>', views.CategoryUpdateView.as_view(), name="update-category")
]