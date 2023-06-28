from django.shortcuts import render
from django.contrib.auth import views as auth_views
from django.contrib.auth.forms import UserCreationForm
from django.views.generic.edit import CreateView
from django.urls import reverse_lazy
# Create your views here.
class LoginView(auth_views.LoginView):
    template_name = 'staff/login.html'

class LogoutView(auth_views.LogoutView):
    template_name='staff/logout.html'

class SignUp(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy("staff:login")
    template_name = "staff/signup.html"