

# Register your models here.
from django.contrib import admin
from .models import Profile

class ProfileAdmin(admin.ModelAdmin):
    list_display = ['user', 'telefon', 'home_adress', 'additional_info']

admin.site.register(Profile, ProfileAdmin)