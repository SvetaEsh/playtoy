from django.urls import path
from . import views

app_name='staff'
urlpatterns = [
    path('login/', views.LoginView.as_view(), name="login"),
    path('logout/', views.LogoutView.as_view(), name="logout"),
    path('signup/', views.SignUp.as_view(), name="signup"),
    path('profile/', views.update_profile, name="profile")
    
    ]

"""
path('showprofile/<int:pk>/', views.ShowProfilePageView.as_view(), name="showprofile"),
"""