from django.urls import path
from . import views

urlpatterns = [path('feedback/', views.send_email)]